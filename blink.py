import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(11, GPIO.OUT) ## Setup GPIO Pin 11 to OUT


for i in range(0,5):## Run loop numTimes

    GPIO.output(11,True)## Switch on pin 11
    time.sleep(10)
    GPIO.output(11,False)## Switch off pin 11
    time.sleep(10)

GPIO.cleanup()
