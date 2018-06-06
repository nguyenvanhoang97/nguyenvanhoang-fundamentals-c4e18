farm = {
    "adult" : 1,
    "kid" : 0
}

n = int(input("Enter your month: "))

for i in range(n):
    tbs = farm["kid"]
    tbl = farm["adult"]

    farm["adult"] = tbl + tbs
    farm["kid"] = tbl

    print("Month " , i , " :" , farm["adult"] , "pair(s) of rabbit")

farm["adult"] = tbl
farm["kid"] = tbs

# for key , val in farm.items():
#     print(key , val)