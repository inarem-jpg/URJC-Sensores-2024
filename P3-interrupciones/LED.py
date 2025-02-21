#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LED_1 = 25
LED_2= 22

if __name__ == '__main__':
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_1, GPIO.OUT)
	GPIO.output(LED_1, GPIO.LOW)
	
	time.sleep(5)
