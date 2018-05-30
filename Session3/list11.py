menu = ["ăn" , "ngủ" , "chơi"]
# n = input("nhap thu ban muon:")
# menu.append(n)
# for i in range(n):
#     print(i+1 , "." , menu[i])
n = int(input("nhap vi tri ban muon sua:"))
menu[n - 1] = input("nhap:  ")
for index, item in enumerate(menu):
    print("{0}. {1}".format(index + 1, item))