# 1  Tính diện tích hình tròn
rad = int(input("nhap ban kinh hinh tron  "))
print("Area = ",rad*rad*3.14)



# 2  Đổi nhiệt độ
c = int(input("nhap do  C  "))
print(c,"C = ",c*5,"F")



# 3.1 Vẽ hình vuông
from turtle import *

shape("turtle")
speed(-1)
color("green")
for i in range(4):

    forward(100)
    left(360 / 4)

mainloop()



# 3.2 Vẽ hình tam giác
from turtle import *

shape("turtle")
speed(-1)
color("green")
for i in range(3):
    
    forward(100)
    left(360 / 3)

mainloop()



# 3.3 Vẽ hình tròn
from turtle import *

shape("turtle")
speed(-1)
color("green")

for i in range(60):
    forward(5)
    left(360 / 60)

mainloop()



# 3.4 Vẽ hình đa vòng kết nối
from turtle import *

shape("turtle")
speed(-1)
color("green")

n = int(input("so vong tron"))
for i in range(n):
    for i in range(60):
        forward(5)
        left(360 / 60)
    left(360 / n)

mainloop()