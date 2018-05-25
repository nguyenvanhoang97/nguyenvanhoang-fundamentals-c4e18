from turtle import *
shape("turtle")
speed(-1)
color("red")

right(30)
forward(100)
for i in range(4):
    left(60)
    forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)
    right(150)
    forward(100)

mainloop()