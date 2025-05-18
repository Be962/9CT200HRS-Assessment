#!/usr/bin/env pybricks-micropython

# Importing modules for the ev3

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (TouchSensor, ColorSensor,
                                 InfraredSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.ev3devices import Motor, UltrasonicSensor

# Reassigning and setting up variables:

ev3 = EV3Brick()
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
DRIVE_SPEED = 100

obstacle_sensor = UltrasonicSensor(Port.S3)

# Setting up the colour sensor:

line_sensor = ColorSensor(Port.S4)
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 1.2


# The followLine function makes the robot follow the black line around the arena, until it sees a block. After it sees the block,
# it will close the distance. Because of the arena set up, the first block will always be yellow.

def followLine():
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 130:
      robot.drive(DRIVE_SPEED, turn_rate)
      wait(10)
    robot.straight(100)

# The turn function is hardcoded. The purpose of this is to move across and collect the red block.

def turn():
    robot.turn(-90)
    robot.straight(435)
    robot.turn(-90)

# The main function sequences the subroutines, putting them in order and organising them.

def main():
    followLine()
    turn()
    followLine()

main()
