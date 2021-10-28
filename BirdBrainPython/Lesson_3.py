from BirdBrain import Finch
from time import sleep
bird=Finch()

"""
exercise 3
bird.setTail(1,0,0,100)
bird.setTail(3,0,0,100)
sleep(2)
bird.stopAll()

exercise 4
r = 100
b = 0
g = 0
for x in range(3):
    bird.setBeak(r,g,b)
    bird.setTail(4,r,g,b)
    sleep(2)
    g = b
    b = r * 1
    r = r * 0
"""
""" 
exercise 5 
userResponse = input("Which tail light (1-4) should be red? ") # Get user input 
number = int(userResponse) # Convert to int
bird.setTail(number , 100,0,0)
sleep(1) 
bird.stopALL() 
it asked me what number of the tail would light up and the number i put changed. 
""" 
""" 
exercise 6 
redLight = input("What should the amount of red be 0-100? ") # Get user input 
greenLight = input("What should the amount of green be 0-100? ") # Get user input 
blueLight = input("What should the amount of blue be 0-100? ") # Get user input 
r = int(redLight) # Convert to int 
g = int(greenLight) # Convert to int 
b = int(blueLight) # Convert to int 
bird.setTail(all,r,g,b) 
bird.setBeak(r,g,b) 
sleep(3) 
bird.stopALL() 
""" 
""" 
exercise 7 
r = 100 
b = 0 
g = 0 
for x in range(4): 
    bird.setBeak(r,g,b) 
    bird.setTail(all,r,g,b) 
    g = b 
    b = r * 1 
    r = r * 0 
    bird.setMove('f',5,100) 
    bird.setTurn('R',90,50) 
"""


bird.stopAll()
