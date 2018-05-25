from turtle import *
shape("turtle")
speed(-1)
n = int(input("nhap so hinh:  "))

for i in range(3 , n , 1):
    for j in range(i):
        forward(100)
        left(360 / i)
        
          
    if i % 2:
        color("red")
    else:
        color("blue")
mainloop()