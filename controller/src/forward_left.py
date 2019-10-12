#!/usr/bin/python3
import time
from adafruit_motorkit import MotorKit
kit = MotorKit()



kit.motor3.throttle = 1

time.sleep(0.5)

kit.motor2.throttle = None
kit.motor1.throttle = None
kit.motor3.throttle = None



exit(0)
