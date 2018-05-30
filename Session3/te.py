size = [5 , 7 , 300 , 90 , 24 , 50 , 75]

ma = size[0]

print(ma)

for i in range(len(size) - 1):
    if ma < size[i + 1]:
        ma = size[i + 1]

print(ma)