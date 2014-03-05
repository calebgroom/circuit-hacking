"""Blink a LED on GPIO on an interval."""

import time
import RPi.GPIO as GPIO

INTERVAL = 1
PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

while True:
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(INTERVAL)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(INTERVAL)
