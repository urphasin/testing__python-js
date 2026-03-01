from turtle import *

forward(200)

left(120)

forward(200)

for i in range(200):
    forward(i)
    left(i+1)
    forward(i+1)
    left(i)
    forward(i+3)
    left(i+3)
    right(40)

