import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0
speed = 0.3
while (count < 100):
			GPIO.output(22,GPIO.HIGH)
			time.sleep(speed)
			GPIO.output(22,GPIO.LOW)
			if (count % 2 > 0): 
				GPIO.output(17,GPIO.HIGH)
				time.sleep(speed)
				GPIO.output(17,GPIO.LOW)
			count = count + 1
			speed = speed - 0.002
