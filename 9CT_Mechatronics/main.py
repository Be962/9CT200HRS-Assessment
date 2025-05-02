#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

line_sensor = ColorSensor(Port.S3)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 100

PROPORTIONAL_GAIN = 1.2

colourNotDetected = False
# Write your program here.
ev3.speaker.beep()


followLine()
turn()
followLine()

def turn():
    robot.turn(-90)
    while colourNotDetected:
        colour()
        return
        robot.drive
        if colour == BLACK:
            colourNotDetected = True
        else:
            colourNotDetected = False
    robot.turn(-90)

def followline():
    deviation = line_sensor.reflection() - threshold

    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 10: 

        robot.drive(DRIVE_SPEED, turn_rate)

        wait(10)
