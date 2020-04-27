
#coder :- Salman Faris
#Connect button on pin number GPIO12

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#Set Gpio 
GPIO.setmode(GPIO.BCM)


#Button
GPIO.setup(18,GPIO.IN)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if(GPIO.input(18)):
        bot.sendMessage(chat_id,text="Button Pressed")
        time.sleep(0.2)
    

bot = telepot.Bot('897944034:AAF6mkevkdAP21L3qJjArolntcfWpLJi_4Y')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
