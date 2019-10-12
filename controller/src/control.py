#!/usr/bin/python3
import time
import pygame
from pygame.locals import *
from adafruit_motorkit import MotorKit
kit = MotorKit()

forward_throttle = 0
steering_throttle = 0 

kit.motor2.throttle = forward_throttle
kit.motor1.throttle = forward_throttle
kit.motor3.throttle = steering_throttle 

pygame.init()

num = 0
done = False
while not done:

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        done = True
    if keys[K_SPACE]:
        forward_throttle = 0
        steering_throttle = 0
    if keys[K_LEFT]:
        steering_throttle += 0.1 
    if keys[K_RIGHT]:
        steering_throttle += -0.1 
    if keys[K_UP]:
        forward_throttle += -0.1
    if keys[K_DOWN]:
        forward_throttle += 0.1
        
    kit.motor2.throttle = forward_throttle 
    kit.motor1.throttle = forward_throttle
    kit.motor3.throttle = steering_throttle

    print(forward_throttle + "::" + steering_throttle)
