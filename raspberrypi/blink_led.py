"""Blink a LED on GPIO on an interval."""
import argparse
import time

import RPi.GPIO as GPIO


def main():
    """Main script execution."""
    parser = argparse.ArgumentParser(description='LED light blinking script.')
    parser.add_argument('--pin', type=int, default=25, help='GPIO pin number')
    parser.add_argument('--interval', type=int, default=1,
                        help='Time in seconds to blink')
    args = parser.parse_args()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(args.pin, GPIO.OUT)

    while True:
        GPIO.output(args.pin, GPIO.HIGH)
        time.sleep(args.interval)
        GPIO.output(args.pin, GPIO.LOW)
        time.sleep(args.interval)

if __name__ == '__main__':
    main()
