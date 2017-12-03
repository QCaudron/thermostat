import sys
from time import sleep
import RPi.GPIO as GPIO

# Scale command-line argument from [0, 1] to [1.55, 11.55]
# ( empirically, the limits of the Futaba 3003 servo )
required_position = float(sys.argv[1]) * 10 + 1.55

# Set up Pin 12 for PWM
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)

# Move the servo, wait for full movement, then stop
pwm.start(required_position)
sleep(1)
pwm.stop()
GPIO.cleanup()
