n = int(input("nhap so:  "))

if n % 2:
    for i in range(n):
        if i % 2:
            print("1" , end = " ")
        else:
            print("0" , end = " ")
else:
    for i in range(n):
        if i % 2:
            print("0" , end = " ")
        else:
            print("1" , end = " ")