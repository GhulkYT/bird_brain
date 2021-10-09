from BirdBrain import Finch
from time import sleep
bird=Finch()


bird.setTail(1,0,0,100)
bird.setTail(3,0,0,100)
sleep(2)
bird.stopAll()