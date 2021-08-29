import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DIGIOUT = 18
GPIO.setup(DIGIOUT, GPIO.IN)
time.sleep(2)

print('[Press CTRL + C to end the script!]')
try: # Main program loop
    while True:
        if GPIO.input(DIGIOUT)==0:
            print('Soil moisture level: HIGH')
            time.sleep(2)
        else:
            print('Soil moisture level: LOW')
            time.sleep(2)
            
except KeyboardInterrupt:
    print('\nScript end!')

finally:
    GPIO.cleanup()
