menu = ["T-Shirt" , "Sweater"]

loop = True

while loop:
    crud = input("Chào mừng bạn, bạn muốn (C, R, U, D)? để thoát nhấn (T) ")   

    if crud == "R":
        for index, item in enumerate(menu):
            print("{0}. {1}".format(index + 1, item))

    elif crud == "C":
        n = input("Nhập mục mới: ")
        menu.append(n)
        for index, item in enumerate(menu):
            print("{0}. {1}".format(index + 1, item))

    elif crud == "U":
        n = int(input("nhập vị trí bạn muốn sửa:"))
        menu[n - 1] = input("nhap:  ")
        for index, item in enumerate(menu):
            print("{0}. {1}".format(index + 1, item))

    elif crud == "D":
        n = int(input("nhập vị trí bạn muốn xóa:  "))
        del menu[n - 1]
        for index, item in enumerate(menu):
            print("{0}. {1}".format(index + 1, item))
    
    elif crud == "T":
        loop = False
