import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	input_state = GPIO.input(27)
	if input_state == False:
		print('Buttion Pressed')
		time.sleep(0.2)
		count = 0
		while (count < 9):
			GPIO.output(22,GPIO.HIGH)
			time.sleep(0.3)
			GPIO.output(22,GPIO.LOW)
			GPIO.output(17,GPIO.HIGH)
			time.sleep(0.3)
			GPIO.output(17,GPIO.LOW)
			count = count + 1
