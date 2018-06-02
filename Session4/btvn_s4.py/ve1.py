from turtle import *
shape("turtle")
speed(-1)
color("green")
# n = int(input("Nhap so hinh ban muon:"))

for i in range(20):
    for j in range(4):
        forward(100)
        right(90)
    right(360 / 20)

mainloop()