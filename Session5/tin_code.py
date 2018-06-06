tin_code = {
    "hc" : "Học",
    "ng" : "Người",
    "pt" : "Phát Triển",
    "any" : "Anh người yêu"
}

while True:
    for key in tin_code:
        print(key , end = "\t")
    print()
    n = input("Enter:  ")
    if n in tin_code:
        print(tin_code[n])
    else:
        print("Not found, you want(Y / N)??")
        cha = input("Enter :")
        if cha == "Y" or cha == "y":
            new = input("Enter key:")
            tin_code[new] = input("Enter value:")    
        else:
            break