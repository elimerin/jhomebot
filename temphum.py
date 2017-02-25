# This is a simple echo bot using the decorator mechanism.
# echo part is modified with #, it will send temperature and humidity.
# It echoes any incoming text messages.
#!/usr/bin/python
import telebot
import Adafruit_DHT as dht
import time

API_TOKEN = '347979536:AAFqwiaufhFVrCnMRKhrvdbBRIpjEBmrmzk'

bot = telebot.TeleBot(API_TOKEN)
suspect="hellO"

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,suspect) 

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
#    bot.reply_to(message, message.text)

@bot.message_handler(commands=['hum','temp'])
def sensor_message(message):
    h,t=dht.read_retry(dht.DHT11,4)
    bot.reply_to(message,"Temp={0:0.1f}*C Humidity={1:0.1f}%".format(t,h))


bot.polling()
