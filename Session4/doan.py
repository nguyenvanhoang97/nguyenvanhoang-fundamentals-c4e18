n = int(input("Nhap 1 so trong khoang 0-100:"))
low = 0
high = 100
mid = (low + high) // 2

while True:
    scl = input("Is {0} your number:".format(mid))
    if scl == "s":
        high = mid
        if high - low <= 1:
            print("you lie!")
            break

    elif scl == "l":
        low = mid
        if high - low <= 1:
            print("you lie!")
            break

    elif scl == "c":
        print("I knew it")
        break

    else:
        break

    mid = (low + high) // 2