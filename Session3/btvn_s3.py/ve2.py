from turtle import *
shape("turtle")
speed(-1)

mau = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(1 , 6):
    fillcolor(mau[i -1])
    begin_fill()
    for j in range(2):
        forward(20)
        left(90)
        forward(40)
        left(90)
    forward(20)
    end_fill()

mainloop()