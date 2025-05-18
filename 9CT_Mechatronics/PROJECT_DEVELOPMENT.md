# 9CT Assessment Task 1

### By Benji Saunders

# Requirements Outline:

## Purpose:

I need to design a program to allow an EV3 Lego Mindstorms robot to transport specific Lego Bricks.  
The robot must use atleast two different sensors and all additional lego must be removable each lesson.  
The robot must be able to sense and avoid the wrong coloured blocks and sense and collect the right coloured blocks.  

## Key Actions:

- **Drive** along a line
- **Detect** the objects
- **Transport** the objects back to the start space

## Functional Requirements:


- **Colour detection:** Detect the line and drive along it to a block.
- **Block detection:** The robot must be able to detect blocks in front of it.
- **Block transportation:** push the block back to the starting area.

## Use Cases:  

<br>

Example 1: 

- **Scenario:** The robot is returning home and encounters an obstacle.
- **Input:** The colour sensor detects the line.
- **Action:** The robot knows to navigate along the line.
- **Expected Outcome** The robot navigates around the course, following the line.

Example 2:

- **Scenario:** The robot is driving a path and detects an object.
- **Input:** The ultrasonic sensor detects the object where it should be.
- **Action:** The robot starts pushing the block.
- **Expected Outcome:** The robot will detect, then move the block.

Example 3:

- **Scenario:** The robot is pushing the first block when it encounters another block.
- **Input:** The ultrasonic sensor detects another block where it should be.
- **Action:** The robot collects the other block.
- **Expected Outcome:** The robot detects and collects the second block

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Robot detects the line |Colour sensor detects the line|The robot drives along the <br> line towards the start/finish line|
|Robot encounters the first object|Ultrasonic sensor detects<br> the first object |The robot will detect, then <br> move the object|
|Robot is pushing the first block <br> and encounters the second along the way to another <br> black line|Colour sensor detects the <br> next line |The robot will stop at the line|

## Non-functional requirements:

1. Efficiency - The robot should not make any unnecessary movements or actions
2. Response time - The robot should be reasonably fast with minimal pausing
3. Accuracy - The robot should precisely execute its commands

# Design:

## Flowcharts (Created with Excalidraw):

#### Flowchart 1: 
![image](https://github.com/user-attachments/assets/c0704380-a5da-46bb-9172-015fc00a385e)
#### Flowchart 2:
![image](https://github.com/user-attachments/assets/353754db-60dc-4c87-8c0d-adde9db4c941)
#### Flowchart 3:
![image](https://github.com/user-attachments/assets/edaa5323-e8fa-4bb5-9340-27b024abb5da)

## Pseudocode:

#### Pseudocode 1: mainline routine
```
BEGIN main
	followLine
	turn
	followLine
END
```
#### Pseudocode 2:
```
BEGIN followLine
	WHILE obstacle_sensor.distance() > 130
		READ distance:
		Drive forwards, turn on black
	ENDWHILE
	Drive forwards 100mm.
END
```
#### Pseudocode 3:
```
BEGIN turn
	Turn -90 degrees
	Drive forwards 435mm
	Turn -90 degrees
END
```
# Testing and debugging (code)

##### Small note/explanation, in the last (3 period) week our project (Mine and Maxi's) was heavily impacted by technical issues, our robot (number 2) was broken, and Mr Groom needed to fix it, he tried 'zapping' the sd card which would not be finished all week. Next we tried all of the other robots, of which also would not work. So finally we had to share with the other groups, which gave us much less time to test and debug leaving us in a scramble and putting strain on the other groups work. Additionally, I tried to get time to catch up on Thursday lunch. On Wednesday I asked the TAS staffroom if we could get supervision for Thursday lunch (as sport cuts out Wednesday lunch). Ms Cartland originally said yes, but later declined as it would be unfair for the other groups, and she had a meeting. I tried these options to catch up however it did not work out. This is why some of the iterations are not great improvements, or may be missing, and there is not a great deal of testing. Additionally Mr Groom said we would discuss the technical issues on Monday (day of submission). Mr Groom and the sub we had on Tuesday, as well as other project groups will confirm this.

### These modules don't change much throughout the tests:
  ```
  #!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

  ```

## Test Case 1:

### Robot detects the line, colour sensor detects the line, the robot drives along the line towards the start/finish.

### Outline: I need to get a function that will follow a line.

### First iteration: Brief idea + setting up/organisation
```
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
def followline():
    deviation = line_sensor.reflection() - threshold

    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 10: 

        robot.drive(DRIVE_SPEED, turn_rate)

        wait(10)
```

### Second iteration: Added beeps for debugging and compacted function. (variables stay the same)

```
def followLine():
    ev3.robot.beep()
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance > 10:
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    robot.ev3.beep()
```

### Third iteration: updating the value the obstacle sensor detects through trial and error(variables stay the same)

```
def followLine():
    ev3.speaker.beep()
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 50:
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    ev3.speaker.beep()
```

### Fourth and final iteration: updated to the last value

```
def followLine():
    ev3.speaker.beep()
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 130:
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    ev3.speaker.beep()

```

### Evaluation:

#### This program meets the criteria in that it will detect and follow the line for a distance. Some errors I had were in getting the program to actually start, as well as knowing how far into the code the program got before stopping. I fixed this with the addition of the beeps which helped the debugging process. Another issue was figuring out what value to put the obstacle sensor so that it would detect the block and not the lego, this was fixed by both moving the lego and adjusting the value. The obstacle sensor reliably detects objects, however the actual follow the line sometimes didnt work, and it was not clear if this was a motor or a code issue. The reliability could definitely be improved with more testing and debugging.

## Test case 2:

### Robot encounters the first object, Ultrasonic sensor detects the first object, The robot will detect, then move the object,

### Outline: I need to make the robot use the ultrasonic sensor to detect a block, then use that to activate specific code.

### First iteration: Basic ideas and organisation.

```
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

line_sensor = ColorSensor(Port.S4)
obstacle_sensor = UltrasonicSensor(Port.S3)


robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 100

PROPORTIONAL_GAIN = 1.2
colourDetected = False

def followline():
    deviation = line_sensor.reflection() - threshold

    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 10: 

        robot.drive(DRIVE_SPEED, turn_rate)

        wait(10)

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
```

### Second iteration: Changed to hardcoding turn, with a placeholder value for both turn and followline. (variables above are the same)

```

def followLine():
    ev3.speaker.beep()
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 50:
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    ev3.speaker.beep()

def turn():
    ev3.speaker.beep()
    colourDetected = False
    robot.turn(90)
    ev3.speaker.beep()
    robot.straight(1000)
    ev3.speaker.beep()
    robot.turn(90)
    ev3.speaker.beep()
```

### Third iteration: polishing the values with real measurements in them.

```
def followLine():
    ev3.speaker.beep()
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 130:
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    robot.straight(100)
    ev3.speaker.beep()


def turn():
    ev3.speaker.beep()
    robot.turn(-90)
    ev3.speaker.beep()
    robot.straight(435)
    ev3.speaker.beep()
    robot.turn(-90)
    ev3.speaker.beep()

```

### Evaluation: This code fits the case. There were a couple errors with this code in the beginning though. For example, the idea in the first iteration to use the colour sensor to detect and stop the robot from crossing the line on the other side of the arena was flawed. The colour sensor was complex and I realised I wouldn't be able to get that method working in the time I had (luckily). I then updated it with hardcoding after measuring the track. The measurements and hardcoding went well, it consistently went the whole way across. However in practice, it rarely got up to that point in the code because of the testing and debugging of previous parts. The program could be improved with better use of the colour sensor, although this solution works.

## Test case 3:

### Robot is pushing the first block and encounters the second along the way to another black line, colour sensor detects the next line, The robot will stop at the line.

### Outline: I need to make the robot collect the second block while pushing the first in one trip.

### First iteration: The idea of detecting the colour at the other line

```
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
```

### Second iteration: Changes to now make it hardcoded with a value, as well as added beeps for debugging and a placeholder value

```
def turn():
    ev3.speaker.beep()
    colourDetected = False
    robot.turn(90)
    ev3.speaker.beep()
    robot.straight(1000)
    ev3.speaker.beep()
    robot.turn(90)
    ev3.speaker.beep()
```

### Third iteration: version with better values, as well as fixing the mistake of turning the wrong way.

```
def turn():
    ev3.speaker.beep()
    robot.turn(-90)
    ev3.speaker.beep()
    robot.straight(435)
    ev3.speaker.beep()
    robot.turn(-90)
    ev3.speaker.beep()
```

### Evaluation: I was not as successful in specifically meeting this requirement, however the outcome is the same. Instead of using the ultrasonic sensor to detect the second block, the second block is just automatically on the path that the robot uses to get back to the start. This likely would have been different if the second block was the green or the blue block. Some errors that have caused trouble are getting the robot lined up with both blocks, to collect them in one trip. What went well was the robot moving across the arena, however it was challenging to actually get to that point with the limited testing. The area that could be improved is the consistency that the robot arrives to this step.

## Peer evaluation:

## Maxi

### When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project?

### 4

#### Maxi has put an exceptional amount of passion into this project. He put full effort into all parts, especially including the mechatronics research task. However in some parts Maxi was challenged when the robot was broken and we were in a tough situation. This is what keeps him from a 5, although 4 is still a good mark.


### When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?

### 5

#### Maxi contributed very well to the research task, and also the various different practice exercises, including the machine assembly.


### When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?

### 3

#### All of Maxi's individual components worked, however the integrated program fell short due to time constraints.

### When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?

### 4

#### Maxi performed well throughout the project. This included the build up through the research task to the lego construction. However the final task caused him trouble when significantly less time was available than originally thought. This was caused by lack of cables and broken robots at times.

