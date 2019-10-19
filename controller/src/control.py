#!/usr/bin/python3
import time

try: 
    from adafruit_motorkit import MotorKit
except:
    print("Error importing motorkit")
    pass

print("Hello World")
# kit = MotorKit()

# forward_throttle = 0
# steering_throttle = 0 

# kit.motor2.throttle = forward_throttle
# kit.motor1.throttle = forward_throttle
# kit.motor3.throttle = steering_throttle 

# num = 0
# done = False
# while not done:        
#     kit.motor2.throttle = forward_throttle 
#     kit.motor1.throttle = forward_throttle
#     kit.motor3.throttle = steering_throttle

#     print(forward_throttle + "::" + steering_throttle)
#     time.sleep(5)