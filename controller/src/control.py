#!/usr/bin/python3
import time
from adafruit_motorkit import MotorKit
kit = MotorKit()



kit.motor1.throttle = 0.5
kit.motor2.throttle = 0.5

time.sleep(10)

kit.motor1.throttle = None
kit.motor2.throttle = None

exit(0)
