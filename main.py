import turtle
import time

duration = 10 # seconds
start_time = time.time()

bob = turtle.Turtle()
bob.color('blue')
bob.shape('turtle')

while time.time() - start_time < duration:
    bob.left(90)
    bob.circle(75)
