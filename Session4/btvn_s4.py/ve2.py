from turtle import*
shape("turtle")
speed(-1)
color("green")

right(135)
count = 200
while True:
    for j in range(4):
        forward(count)
        right(90)
    right(10)
    count = count - 4
    if count < 4:
        break
mainloop()