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

"""

