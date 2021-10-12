from BirdBrain import Finch
from time import sleep
bird=Finch()

"""
exercise 3
bird.setTail(1,0,0,100)
bird.setTail(3,0,0,100)
sleep(2)
bird.stopAll()
"""
r = 100
b = 0
g = 0
for x in range(3):
    bird.setBeak(all,r,b,g)
    bird.setTail(all,r,b,g)
    sleep(2)
    b = r * 1
    r = r * 0
    g = g + 50

bird.stopAll()
