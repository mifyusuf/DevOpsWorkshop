import time
import RPi.GPIO as GPIO       ## Import GPIO library

Led1 = 11
Led2 = 13
Led3 = 15
class Led(object):
	def set(self, PIN):
		# Initialize lock servo and button.
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(PIN, GPIO.OUT)
		GPIO.output(PIN,GPIO.LOW)
	def LedOn(self, PIN):
		LedOn = GPIO.output(PIN,GPIO.HIGH)
	def LedOff(self, PIN):
		LedOff = GPIO.output(PIN,GPIO.LOW)
Led().set(Led1)
Led().set(Led2)
Led().set(Led3)
		
while True:
	Led().LedOn(Led1)  ## Turn on Led
	time.sleep(0.5)  
	Led().LedOff(Led1)	## Wait for one second
	Led().LedOn(Led2)
	time.sleep(0.5)
	Led().LedOff(Led2)
	Led().LedOn(Led3)
	time.sleep(0.5)
	Led().LedOff(Led3)
	
