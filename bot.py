import os, json, re, requests, base64
from datetime import datetime
import telebot
from telebot import types
import anthropic
import firebase_admin
from firebase_admin import credentials, firestore

# ── Init ──────────────────────────────────────────────────────────────────────
BOT_TOKEN = os.environ['BOT_TOKEN']
ANTH_KEY  = os.environ['ANTHROPIC_KEY']

cred_dict = json.loads(os.environ['FIREBASE_CREDS'])
cred_dict['private_key'] = cred_dict['private_key'].replace('\\n', '\n')
firebase_admin.initialize_app(credentials.Certificate(cred_dict))
db  = firestore.client()
DOC = db.collection('emis_money').document('shared')

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown')
ac  = anthropic.Anthropic(api_key=ANTH_KEY)

# ── Firestore helpers ─────────────────────────────────────────────────────────
def get_data():
    snap = DOC.get()
    base = {'expenses': [], 'balances': {'juli': 0, 'camilo': 0}, 'user_map': {}}
    return {**base, **(snap.to_dict() if snap.exists else {})}

def get_person(cid):
    return get_data()['user_map'].get(str(cid))

def set_person(cid, name):
    um = get_data()['user_map']
    um[str(cid)] = name
    DOC.set({'user_map': um}, merge=True)

def add_expense(person, amount, desc):
    now = datetime.now()
    exp = {
        'id': f'{now.timestamp():.3f}',
        'person': person,
        'amount': amount,
        'description': desc,
        'date': now.strftime('%d/%m/%Y'),
        'month': now.strftime('%Y-%m'),
    }
    exps = get_data()['expenses']
    exps.append(exp)
    DOC.set({'expenses': exps}, merge=True)
    return exp

def undo_last(person):
    data = get_data()
    exps = data['expenses']
    mine = [e for e in exps if e['person'] in [person, 'together']]
    if not mine:
        return None
    last = sorted(mine, key=lambda e: e['id'])[-1]
    DOC.set({'expenses': [e for e in exps if e['id'] != last['id']]}, merge=True)
    return last

def month_summary():
    data  = get_data()
    month = datetime.now().strftime('%Y-%m')
    exps  = [e for e in data['expenses'] if e.get('month') == month]
    return {
        'juli':     sum(e['amount'] for e in exps if e['person'] == 'juli'),
        'camilo':   sum(e['amount'] for e in exps if e['person'] == 'camilo'),
        'together': sum(e['amount'] for e in exps if e['person'] == 'together'),
        'balances': data['balances'],
        'recent':   sorted(exps, key=lambda e: e['id'], reverse=True)[:5],
    }

def require_person(msg):
    p = get_person(msg.chat.id)
    if not p:
        mk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        mk.add('Juli', 'Camilo')
        bot.send_message(msg.chat.id, "Who are you?", reply_markup=mk)
    return p

# ── /start ────────────────────────────────────────────────────────────────────
@bot.message_handler(commands=['start'])
def cmd_start(msg):
    p = get_person(msg.chat.id)
    if p:
        bot.send_message(msg.chat.id,
            f"Welcome back, *{p.title()}!* 💰\n\n"
            "Send me a transaction:\n"
            "• *50 groceries* — your expense\n"
            "• *together 80 dinner* — shared 50/50\n"
            "• *balance 1500* — update your card balance\n"
            "• Or send a photo of a receipt 📸\n\n"
            "/summary — this month's totals\n"
            "/undo — delete your last entry")
    else:
        mk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        mk.add('Juli', 'Camilo')
        bot.send_message(msg.chat.id, "👋 Hi! Who are you?", reply_markup=mk)

# ── Registration ──────────────────────────────────────────────────────────────
@bot.message_handler(func=lambda m: m.text in ('Juli', 'Camilo') and not get_person(m.chat.id))
def register(msg):
    set_person(msg.chat.id, msg.text.lower())
    bot.send_message(msg.chat.id,
        f"✅ Got it, *{msg.text}!* You're all set.\n\n"
        "Send transactions like:\n"
        "• *50 groceries*\n"
        "• *together 80 dinner*\n"
        "• *balance 1500*\n"
        "• Or a photo of a receipt 📸",
        reply_markup=types.ReplyKeyboardRemove())

# ── /summary ──────────────────────────────────────────────────────────────────
@bot.message_handler(commands=['summary'])
def cmd_summary(msg):
    s   = month_summary()
    tog = s['together']
    mon = datetime.now().strftime('%B %Y')
    text  = f"📊 *{mon}*\n\n"
    text += f"👤 Juli:     *A${s['juli']:.2f}*\n"
    text += f"👤 Camilo:   *A${s['camilo']:.2f}*\n"
    text += f"🤝 Together: *A${tog:.2f}* (A${tog/2:.2f} each)\n\n"
    text += "💳 *Card Balances*\n"
    text += f"Juli:   A${s['balances'].get('juli', 0):.2f}\n"
    text += f"Camilo: A${s['balances'].get('camilo', 0):.2f}"
    if s['recent']:
        text += "\n\n🕐 *Recent*\n"
        for e in s['recent']:
            text += f"• {e['description']} — A${e['amount']:.2f} ({e['person'].title()})\n"
    bot.send_message(msg.chat.id, text)

# ── /undo ─────────────────────────────────────────────────────────────────────
@bot.message_handler(commands=['undo'])
def cmd_undo(msg):
    p = require_person(msg)
    if not p:
        return
    deleted = undo_last(p)
    if deleted:
        bot.send_message(msg.chat.id,
            f"✅ Deleted: *{deleted['description']}* — A${deleted['amount']:.2f}")
    else:
        bot.send_message(msg.chat.id, "Nothing to undo.")

# ── Photos ────────────────────────────────────────────────────────────────────
@bot.message_handler(content_types=['photo'])
def handle_photo(msg):
    p = require_person(msg)
    if not p:
        return
    wait = bot.send_message(msg.chat.id, "⏳ Reading transaction…")
    try:
        fi   = bot.get_file(msg.photo[-1].file_id)
        data = requests.get(
            f"https://api.telegram.org/file/bot{BOT_TOKEN}/{fi.file_path}"
        ).content
        b64  = base64.b64encode(data).decode()
        resp = ac.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=128,
            messages=[{"role": "user", "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64}},
                {"type": "text",  "text": "Bank transaction screenshot. Reply ONLY with JSON: {\"description\":\"merchant name\",\"amount\":0.00}"}
            ]}]
        )
        parsed = json.loads(resp.content[0].text.strip())
        amt  = float(parsed['amount'])
        desc = str(parsed['description'])
        bot.delete_message(msg.chat.id, wait.message_id)
        mk = types.InlineKeyboardMarkup()
        mk.row(
            types.InlineKeyboardButton(f"✅ Mine ({p.title()})", callback_data=f"sv|{p}|{amt}|{desc[:40]}"),
            types.InlineKeyboardButton("🤝 Together",           callback_data=f"sv|together|{amt}|{desc[:40]}")
        )
        mk.row(types.InlineKeyboardButton("❌ Cancel", callback_data="cancel"))
        bot.send_message(msg.chat.id, f"📋 *{desc}*\nA${amt:.2f}\n\nSave as?", reply_markup=mk)
    except Exception:
        bot.edit_message_text(
            "⚠️ Couldn't read it. Type manually:\n*50 groceries* or *together 80 dinner*",
            msg.chat.id, wait.message_id)

@bot.callback_query_handler(func=lambda c: True)
def handle_cb(call):
    cid = call.message.chat.id
    if call.data == 'cancel':
        bot.edit_message_text("❌ Cancelled.", cid, call.message.message_id)
        return
    _, person, amt_str, desc = call.data.split('|', 3)
    amt = float(amt_str)
    add_expense(person, amt, desc)
    extra = f" (A${amt/2:.2f} each)" if person == 'together' else ""
    bot.edit_message_text(
        f"✅ *{desc}* — A${amt:.2f} → {person.title()}{extra}",
        cid, call.message.message_id)

# ── Text messages ─────────────────────────────────────────────────────────────
@bot.message_handler(func=lambda m: True)
def handle_text(msg):
    p = require_person(msg)
    if not p:
        return
    t = msg.text.strip().lower()

    # balance 1500
    m = re.match(r'^balance\s+(\d+\.?\d*)$', t)
    if m:
        amt = float(m.group(1))
        bal = get_data()['balances']
        bal[p] = amt
        DOC.set({'balances': bal}, merge=True)
        bot.send_message(msg.chat.id, f"✅ {p.title()}'s balance updated: *A${amt:.2f}*")
        return

    # together 80 dinner
    m = re.match(r'^together\s+(\d+\.?\d*)\s+(.+)$', t)
    if m:
        amt, desc = float(m.group(1)), m.group(2).title()
        add_expense('together', amt, desc)
        bot.send_message(msg.chat.id,
            f"✅ *{desc}* — A${amt:.2f} shared (A${amt/2:.2f} each)")
        return

    # [person] amount description
    m = re.match(r'^(?:(juli|camilo)\s+)?(\d+\.?\d*)\s+(.+)$', t)
    if m:
        target = m.group(1) or p
        amt, desc = float(m.group(2)), m.group(3).title()
        add_expense(target, amt, desc)
        bot.send_message(msg.chat.id, f"✅ *{desc}* — A${amt:.2f} → {target.title()}")
        return

    bot.send_message(msg.chat.id,
        "Try:\n• *50 groceries*\n• *together 80 dinner*\n• *balance 1500*\n/summary  /undo")

# ── Run ───────────────────────────────────────────────────────────────────────
print("🤖 Emi's Money Bot is running!")
bot.infinity_polling(timeout=20, long_polling_timeout=15)
