from random import randint
numb = randint(0,100)
loop = True
count = 0
print(numb)

while loop:
    if count < 7:
        n = int(input("nhap so:  "))

        if n < numb:
            print("so lon hon n")
        elif n > numb:
            print("so nho hon n")
        else:
            print("bingo")
            loop = False
    else:
        print("ban thua")
        loop = False
    
    count += 1