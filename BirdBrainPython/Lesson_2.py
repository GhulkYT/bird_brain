from BirdBrain import Finch
bird=Finch()
#addition = +, subtraction = -, multiplication = *, division = /,Modulo = %,
distance = bird.getDistance()
rightLight = bird.getLight('R')
leftLight = bird.getLight('L')
buttonA = bird.getButton('A')
orientation = bird.getOrientation()
rightEncode = bird.getEncoder('R')
diffrence = rightLight - leftLight
mean = rightLight + leftLight / 2
print("mean: ", mean)
"""
print("idk")
print("distance: ", distance)
print("rightlight: ", rightLight)
print("leftlight: ", leftLight)
print("ButtonA: ", buttonA)
print("Orientation: ", orientation)
print("RightWheel: ", rightEncode)

print("idk")
print("distance: ",type(distance))
print("rightlight: ",type(rightLight))
print("leftlight: ", type(leftLight))
print("ButtonA: ", type(buttonA))
print("Orientation: ", type(orientation))
print("RightWheel: ", type(rightEncode))
"""