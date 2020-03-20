# coding: utf8
import telebot
import process
import os

token = '963784896:AAEqcmeybGi9gPzMirnPJ7ObAYDitmQlcm4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help', 'text', 'minitrip'])
def start_message(message):
    global switcher
    if message.text == "/start":
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "Перешли мне пост из t.me//economika!")
    elif message.text == '/text':
        bot.send_chat_action(message.chat.id, "typing")
        text = input_str
        array = process.parse_string(text)
        text = process.economy(array) + process.find_hastags(text)
        bot.send_message(message.chat.id, text)
    elif message.text == '/minitrip':
        switcher = 'minitrip'
    elif message.text == '/economy':
        switcher = 'economy'


@bot.message_handler(content_types=['text'])
def remember_input_str(message):
    global input_str
    input_str = message.text


@bot.message_handler(content_types=['video'])
def do(message):
    bot.send_chat_action(message.chat.id, 'typing')
    text = message.caption
    array = process.parse_string(text)
    text = process.economy(array) + process.find_hastags(text)
    bot.send_chat_action(message.chat.id, "typing")
    try:
        file_id_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_id_info.file_path)
        with open(f'1.MOV', 'wb') as new_file:
            bot.send_chat_action(message.chat.id, 'typing')
            new_file.write(downloaded_file)

        process.get_first_frame()

        process.cut_png()

        process.do_image_png(input_str=input_str)

        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_photo(message.chat.id, open('first_done.png', 'rb'))

        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_photo(message.chat.id, open('second_done.png', 'rb'))

        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_photo(message.chat.id, open('third_done.png', 'rb'))

        os.remove('first_done.png')
        os.remove('second_done.png')
        os.remove('third_done.png')

        bot.send_message(message.chat.id, text)

    except Exception as ex:
        bot.send_message(message.chat.id, "[!] error - {}".format(str(ex)))


@bot.message_handler(content_types=['document'])
def do(message):
    try:
        file_id_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_id_info.file_path)
        with open(f'first_frame.png', 'wb') as new_file:
            bot.send_chat_action(message.chat.id, 'typing')
            new_file.write(downloaded_file)

        process.cut_png()

        process.do_image_png(input_str=input_str, switcher=switcher)

        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_photo(message.chat.id, open('first_done.png', 'rb'))

        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_photo(message.chat.id, open('second_done.png', 'rb'))

        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_photo(message.chat.id, open('third_done.png', 'rb'))

        os.remove('first_done.png')
        os.remove('second_done.png')
        os.remove('third_done.png')

    except Exception as ex:
        bot.send_message(message.chat.id, "[!] error - {}".format(str(ex)))


bot.polling()
