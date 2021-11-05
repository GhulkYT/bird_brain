from BirdBrain import Finch
from time import sleep
bird=Finch()
"""
excercise 1 :
Try out the code shown above. The Finch moves in a straight line when the 
speed of the left and right wheels are the same. What happens when one speed 
is positive and the other speed is negative?
bird.setMotors(-50,50)
sleep(5)
bird.stop()
"""
"""
excercise 2
Write a program that asks the user for the speeds of the right and left 
wheels and then moves the Finch for 2 seconds with those speeds. 
What happens when the right and left speeds are close together?
What happens when they are far apart?

leftWheel = int(input("left wheel speed: "))
rightWheel = int(input("right wheel speed: "))
bird.setMotors(leftWheel,rightWheel)
sleep(2)
bird.stop()

closer together the bigger
but when the speeds are far apart the circles bigger
"""
"""
excercise 3
Write a program to make the Finch move in a figure-8 pattern.
first im going to set the motors to 5 90
then im going to tell it to sleep for 1 second
then im going to set the motors to 90 5 
then im going to tell it to sleep for 1 second
then im going to stop the motors

bird.setMotors(5,90)
sleep(1)
bird.setMotors(90,5)
sleep(1)
bird.stop()
"""
"""
exercise 4
What do you think the code below will do?
Make a hypothesis, and then try it out.
i think if you dont put g then the beak wont change colors
but if yo do it will turn green
 
color = input("Please enter a letter: ")
if (color == 'g'):
    bird.setBeak(0,100,0)
else:
    print('Sorry, that is not my favorite Letter!')
sleep(1)
bird.stopAll()
"""
 
 
"""
exercise 5
 
Write a program that asks the user to enter r or l.
If the user enters ‘r’, the Finch should make a wide turn to the right.
Otherwise, the Finch should make a wide turn to the left.
 
 
turn = input("Please enter a letter: ")
if (turn == 'r'):
    bird.setMotors(5,90)
else if (turn == 'l'):
    bird.setMotors(90,5)
else:
    print('gotta put l or r')
sleep(1)
bird.stopAll()
"""
 
"""
exercise 6
Try out this code. Then modify it so that only slow speeds are valid.
 
 
userResponse = input("Please enter a speed (0 to 10): ")
speed = int(userResponse)
if (speed >= 0) and (speed <= 10): # If both are true
 
    bird.setMotors(speed, speed) # Move forward
    sleep(1)
    bird.stop()
 
else: # Otherwise
 
print("That speed is not valid!") # Error
"""
 
"""
exercise 7
Write a program that asks the user for a wheel speed between 0 and 50.
If the user enters an invalid value, the program should print an error.
Otherwise, the Finch should turn for 5 seconds with the speed of the left wheel equal
to the speed entered by the user and the speed of the right wheel equal to twice the entered speed.
 
userResponse = input("Please enter a speed (0 to 50): ")
speed = int(userResponse)
if (speed >= 0) and (speed <= 50): # If both are true
    right = speed * 2
    bird.setMotors(speed, right) # Move forward
    sleep(1)
    bird.stop()
 
else: # Otherwise
 
print("That speed is not valid!") # Error
 
"""
 
"""
exercise 8
 
bird.setMotors(5,90)
sleep(1)
bird.setMotors(90,5)
sleep(1)
bird.setMotors(5,90)
sleep(1)
bird.setMotors(90,5)
sleep(1)
bird.setMotors(5,90)
sleep(1)
bird.setMotors(90,5)
sleep(1)
bird.stop()
"""
 



