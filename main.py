import telebot, random
BOT_TOKEN = "5124389784:AAFj2-GJPAC3NRMsmbmshREjzshjvvBm6-U"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: m.text and ("المطور" in m.text or "المبرمج" in m.text))
def dev(m):
    bot.reply_to(m, "المطور: @FFBBD")

@bot.message_handler(func=lambda m: m.text and "العاب" in m.text)
def games(m):
    bot.reply_to(m, "/سؤال /نكتة /حظ /حجر /رقم /حب")

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "اهلا بك! اكتب المطور او العاب")

@bot.message_handler(commands=['سؤال'])
def q(m):
    bot.reply_to(m, random.choice(["عاصمة اليمن؟","كم عدد الكواكب؟","اسرع حيوان؟"]))

@bot.message_handler(commands=['نكتة'])
def joke(m):
    bot.reply_to(m, "نكتة: محشش سألوه وش اصعب شي قال اثبت اني مو محشش")

@bot.message_handler(commands=['حظ'])
def luck(m):
    bot.reply_to(m, f"حظك اليوم {random.randint(1,100)}%")

@bot.message_handler(commands=['حجر'])
def rps(m):
    bot.reply_to(m, random.choice(["حجر","ورقة","مقص"]))

@bot.message_handler(commands=['رقم'])
def num(m):
    bot.reply_to(m, str(random.randint(1,10)))

@bot.message_handler(commands=['حب'])
def love(m):
    bot.reply_to(m, f"نسبة الحب {random.randint(10,100)}%")

print("Bot is running...")
bot.infinity_polling()
