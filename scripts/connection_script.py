# libraries
import RPi.GPIO as GPIO
import time

# pin number
pir_input_pin = 11

# configurations
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_input_pin, GPIO.IN)

# vars
motion_count = 0

# when there is motion, print "Motion"
while(True):
	i = GPIO.input(pir_input_pin)
	if(i == 1):		# if motion found
		motion_count += 1
		print(motion_count, "Motion")
	time.sleep(1)	# sleep for 1 second
