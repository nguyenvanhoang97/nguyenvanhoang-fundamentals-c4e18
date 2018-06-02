user = "123456"
pa = "654321"

loop = True
count = 0

us = input("Nhap username: ")
p = input("Nhap password:")

while loop:

    if count <= 2:
        if us == user:
            if pa == p:
                print("Dang nhap thanh cong")
                loop = False

            else:
                print("Sai password")
                us = input("Nhap username: ")
                p = input("Nhap password:")

        else:
            print("Sai username")
            us = input("Nhap username: ")
            p = input("Nhap password:")
    
    else:
        print("Dang nhap qua so lan")

    count += 1