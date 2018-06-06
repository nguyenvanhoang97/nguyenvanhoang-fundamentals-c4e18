# person = ["Quý" , 20 , 0 , "Vĩnh Phúc" , 2 , ["Manga" , "Coding"] , 3 , 20]

#dictionary
person = {
    "name":"Quý",
    "age":20,
    "ex":0,
    "favs":["manga" , "coding"]
}

# print(person)

# name = person["name"]
# print(name)

person["length"] = 20 #coi như 1 biến có thể thay đổi giá trị
# print(person)

# del person["length"]
# key = "length"
# if key in person:
#     print(person[key])
# else:
#     print("not found")

# for k in person:
#     print(k , person[k])

# for v in person.values():
#     print(v)

for key , val in person.items():
    print(key , val)