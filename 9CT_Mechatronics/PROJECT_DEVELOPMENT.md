# 9CT Assessment Task 1

### By Benji Saunders

## Purpose:

I need to design a program to allow an EV3 Lego Mindstorms robot to transport specific Lego Bricks.  
The robot must use atleast two different sensors and all additional lego must be removable each lesson.  
The robot must be able to sense and avoid the wrong coloured blocks and sense and collect the right coloured blocks.  

## Key Actions:

- **Detect** the correct object
- **Transport** the object back to the start space
- **Drive** around until an object is detected

## Functional Requirements:


- **Colour detection:** Detect the object and determine if it is the correct block to be transported.
- **Block transportation:** Once the block has been recognized, push it back to the starting area.
- **Drive to destination:** The robot must be able to drive around obstacles, to the correct place.

## Use Cases:  

<br>

Example 1: 
- **Scenario:** The robot is driving a path and detects an object.
- **Input:** The ultrasonic sensor detects the object where it should be.
- **Action:** The robot starts pushing the block.
- **Expected Outcome:** The robot will detect, then move the block.

Example 2:

- **Scenario:** The robot is pushing the first block when it encounters another block.
- **Input:** The ultrasonic sensor detects another block where it should be.
- **Action:** The robot collects the other block.
- **Expected Outcome:** The robot detects and collects the second block

Example 3:

- **Scenario:** The robot is returning home and encounters an obstacle.
- **Input:** The ultrasonic sensor detects another block.
- **Action:** The robot knows the third object is an obstacle, and navigates around it.
- **Expected Outcome** The robot navigates around the obstacle, returning to the start area.

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Robot encounters the first object|Ultrasonic sensor detects<br> the first object |The robot will detect, then <br> move the object|
|Robot is pushing the first block <br> and encounters the second|Ultrasonic sensor detects the <br> next block where it should be|The robot will start pushing <br> the next block as well|
|Robot is pushing the first and <br> second block, encounters the third|Ultrasonic detects the block|The robot navigates around the <br> block towards the start/finish line|

## Non-functional requirements:

1. Efficiency - The robot should not make any unnecessary movements or actions
2. Response time - The robot should be reasonably fast with minimal pausing
3. Accuracy - The robot should precisely execute its commands