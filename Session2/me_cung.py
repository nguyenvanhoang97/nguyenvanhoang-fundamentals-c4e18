from turtle import *

shape("turtle")
speed(-1)
color("green")
n=500

for i in range(0 , n , 10):
    forward(i)
    left(90)


mainloop()