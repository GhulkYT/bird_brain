from BirdBrain import Finch
bird = Finch()
"""
Lesson 3
bird.setTurn('R',360,100)
bird.setTurn('L',360,100)
"""

for x in range(4):
    bird.setMove('f',5,100)
    bird.setTurn('R',90,50)
