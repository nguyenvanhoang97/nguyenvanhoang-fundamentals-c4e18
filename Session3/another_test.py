# food1 = "salad"
# food2 = "choco"
# food3 = "sò"
# food4 = "Mì tôm"
# food5 = "Phở"

#list (array)
#CRUD
#create
#read
#update
#delete
menu = ["salad" , "choco" , "sò" , "Mì tôm" , "phở"]
#seperator
# print(*menu , sep = " , ")
# print(len(menu))

#thêm
# menu.append("bánh mướt")
# print(*menu , sep = " , ")

#in ra số phần tử
# print(len(menu))

#indexing đánh số các phần tử
# first_item = menu[-1]
# print(first_item)

# for i in range(5):
#     print(i+1 , "." , menu[i])


#string formatting
# for i in range(len(menu)):
#     print("{0}. {1}".format(i + 1,menu[i]))

# print("* " * 20)

for index, item in enumerate(menu):
    print("{0}. {1}".format(index + 1, item))

# print("* " * 20)

# for item in menu:
#     print(item)
print("*" * 20)
#update
menu[2] = "cua"
for index, item in enumerate(menu):
    print("{0}. {1}".format(index + 1, item))