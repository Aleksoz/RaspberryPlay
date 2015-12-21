import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPI0.setup(17,GPIO.OUT)

GPIO.output(22,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
