# from turtle import *

# shape("turtle")
# speed(-1)
# color("green")
# fillcolor("green")
# begin_fill()

# for i in range(200):
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     right(7)

# end_fill()


# mainloop()
from turtle import *

n = int(input("nhap so canh cua hinh"))

shape("turtle")
speed(-1)
color("green")
fillcolor("green")

for i in range(n):
    forward(50)
    left(360/n)


mainloop()