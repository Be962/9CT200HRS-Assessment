#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (TouchSensor, ColorSensor,
                                 InfraredSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.ev3devices import Motor, UltrasonicSensor
from ev3dev2.light import Light, Color

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

colour = ColorSensor(Port.S3)
cs = ColorSensor(Port.S3)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 100

PROPORTIONAL_GAIN = 1.2

obstacle_sensor = UltrasonicSensor(Port.S4)

color_value = cs.Color

colourNotDetected = False
# Write your program here.





def turn():
    colourNotDetected = False
    ev3.speaker.beep()
    robot.turn(-90)
    while colourNotDetected == False:
        ev3.speaker.beep()
        colour.reflection()
        return
        robot.drive(DRIVE_SPEED, 0)
        if colour == BLACK:
            colourNotDetected = True
        else:
            colourNotDetected = False
    robot.turn(-90)

def followLine():
    ev3.speaker.beep()
    deviation = line_sensor.reflection() - threshold

    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 300:
        wait(10)



        robot.drive(DRIVE_SPEED, turn_rate)

def main():
    while True:
        if color_value == Color.BLACK:
            ev3.robot.beep()



main()
