
from adafruit_motorkit import MotorKit
kit = MotorKit()


kit.motor1.throttle = 0.5

sleep(2000)

kit.motor1.throttle = None
