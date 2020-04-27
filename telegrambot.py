#coder :- Salman Faris

import sys
import time
import telepot
import RPi.GPIO as GPIO
import subprocess
import random 

#sound
#audio_path = '/home/pi/TelegramBot/leprous_at_the_bottom.mp3'
#audio_path = '/home/pi/TelegramBot/lsd_genius.mp3'
audio_path = ['/home/pi/TelegramBot/maks_nezemnaja.mp3','/home/pi/TelegramBot/lsd_genius.mp3', '/home/pi/TelegramBot/leprous_at_the_bottom.mp3']
song = random.choice(audio_path)

def play_on(song):
    print('playing song',song)
    subprocess.call(['omxplayer',song])
    #return 'playing song'

def play_off():#should terminate the subprocess but it works not properly  
    print('stop playing song')
    subprocess.Popen('killall "omxplayer.bin"')
    #return 'stop playing song'

#LED
def on(pin):
        print('The LED %s turn on' % pin)
        GPIO.output(pin,GPIO.HIGH)
        return 'The LED %s turn on' % pin
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return 'The LED %s turn off' % pin
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(18, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)
    command = command.lower()
    if command == 'on':
       bot.sendMessage(chat_id, on(18), play_on(song))
    elif command =='off':
       bot.sendMessage(chat_id, off(18),sys.exit())
    else:
       bot.sendMessage(chat_id, 'Please choose the option: "on" or "off' )
bot = telepot.Bot('897944034:AAF6mkevkdAP21L3qJjArolntcfWpLJi_4Y')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
    
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()
