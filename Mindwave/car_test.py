import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

GPIO.setup(38,GPIO.OUT)
servo2 = GPIO.PWM(38,50)
servo1.start(0) #Right Wheel
servo2.start(0) #Left wheel
print("Wait for 1 second")
time.sleep(1)

## The speeds 

## 4 and 10 are similar
## 9 and 5 are similar
## 7 is stop
## 3 and 12 are max 



# duty = 3


#three different speeds
# while duty <= 11:
#     print(duty)
#     servo2.ChangeDutyCycle(duty)
#     servo1.ChangeDutyCycle(14-duty)
#     time.sleep(
# )
#     duty += 1
state = 1

while state <= 3:

    if state == 1:

        #State 1 Fastest state
        servo1.ChangeDutyCycle(4)   #Right Wheel
        servo2.ChangeDutyCycle(13)  #Left wheel
        time.sleep(10)
    
    elif state == 2:
        # State 2 2nd fastest    

        servo1.ChangeDutyCycle(4.5)   #Right Wheel
        servo2.ChangeDutyCycle(10)  #Left wheel
        time.sleep(10)

    elif state == 3:
        # State 3

        servo1.ChangeDutyCycle(5)   #Right Wheel
        servo2.ChangeDutyCycle(9.5)  #Left wheel
        time.sleep(10)
        
    state += 1

# Changes to 180 degrees in 10 steps
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
servo1.stop()
servo2.stop()
GPIO.cleanup()
print("Done")