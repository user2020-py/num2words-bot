import telebot
from num2words import num2words
import config
bot = telebot.TeleBot(config.token)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('📱Yordam📱','📡 Kanal 📡')
keyboard.row('🖤 Dasturchi 🖤')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Xush kelibsiz, '+str(message.chat.first_name), reply_markup=keyboard)

@bot.message_handler(commands=['lang'])
def send_langs(message):
    lang_list = '''en - (English, default)
ar - (Arabic)
cz - (Czech)
de - (German)
dk - (Danish)
en_GB - (English - Great Britain)
en_IN - (English - India)
es - (Spanish)
es_CO - (Spanish - Colombia)
es_VE - (Spanish - Venezuela)
eu - (EURO)
fi - (Finnish)
fr - (French)
fr_CH - (French - Switzerland)
fr_BE - (French - Belgium)
fr_DZ - (French - Algeria)
he - (Hebrew)
id - (Indonesian)
it - (Italian)
ja - (Japanese)
kn - (Kannada)
ko - (Korean)
lt - (Lithuanian)
lv - (Latvian)
no - (Norwegian)
pl - (Polish)
pt - (Portuguese)
pt_BR - (Portuguese - Brazilian)
sl - (Slovene)
sr - (Serbian)
ro - (Romanian)
ru - (Russian)
sl - (Slovene)
tr - (Turkish)
th - (Thai)
vi - (Vietnamese)
nl - (Dutch)
uk - (Ukrainian)'''
    bot.send_message(message.chat.id, lang_list, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
	try:
		res1 = str(message.text).split('-')
		lang = res1[0]
		num = res1[1]
		#Convert INT or FLOAT
		try:
			num = int(num)
		except:
			num = float(num)

		res1 = num2words(num, lang=lang)
		bot.send_message(message.chat.id, res1, reply_markup=keyboard)

	except:
		if message.text == '📱Yordam📱':
		    help_t = '''🤔 Botdan qanday foydalaniladi
Misol: til-son
Yani: ru-123 yoki en-123 bo'lishi mumkin.
➖➖➖➖
👉 Boshqa tillar: /lang'''
		    bot.send_message(message.chat.id, help_t, reply_markup=keyboard)
		elif message.text == '📡 Kanal 📡':
		    bot.send_message(message.chat.id, '👉 https://t.me/python_dasturlash_darslari', reply_markup=keyboard)
		elif message.text == '🖤 Dasturchi 🖤':
		    bot.send_message(message.chat.id, '👉 @junior_coder_2007', reply_markup=keyboard)
		else:
		    bot.send_message(message.chat.id, 'Xato Buyruq', reply_markup=keyboard)

if __name__ == '__main__':
    bot.polling(none_stop=True)

