import RPi.GPIO as GPIO
import time
import telepot

bot = telepot.Bot('Api telegram bot')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.HIGH)
GPIO.output(20,GPIO.HIGH)
time.sleep(2)
GPIO.output(20,GPIO.LOW)
time.sleep(3)
GPIO.output(21,GPIO.LOW)
bot.sendMessage(-120421181, text="DOOR UNLOCKED")
GPIO.cleanup()

