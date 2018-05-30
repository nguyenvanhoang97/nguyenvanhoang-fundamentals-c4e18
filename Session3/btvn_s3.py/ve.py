from turtle import *
shape("turtle")
speed(-1)

mau = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(3 , 8 , 1):
    for j in range(i):
        forward(100)
        left(360 / i)
        color(mau[i - 3])

mainloop()