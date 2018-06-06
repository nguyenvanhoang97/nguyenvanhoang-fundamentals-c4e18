prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0
accom = 0
for k in prices:
    for j in stock:
        if k == j:
            print(k)
            print("price" , prices[k])
            print("stock" , stock[j])
            accom = prices[k] * stock[j]
            total += accom

print(total)


