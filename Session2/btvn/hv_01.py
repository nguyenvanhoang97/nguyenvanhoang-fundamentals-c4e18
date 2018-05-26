n = int(input("nhap so ban muon:  "))


for i in range(n):
    if i % 2:
        for j in range(n):
            if j % 2:
                print("1" , end = " ")
            else:
                print("0" , end = " ")
        print()
    else:
        for j in range(n):
            if j % 2:
                print("0" , end = " ")
            else:
                print("1" , end = " ")
        print()