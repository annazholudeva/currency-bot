import telebot

TOKEN = '5877306663:AAGErScQdCAogK5-AXzN9-COLBLUkJmLevs'

bot = telebot.TeleBot(TOKEN)

keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB'
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в формате: \n<имя валюты> ' \
           '\n <в какую валюту перевести>' \
           '\n <количество переводимой валюты>'\
           '\n Увидеть список доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')


bot.polling()
