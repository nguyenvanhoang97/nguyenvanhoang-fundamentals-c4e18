li = [10 , 2 , -5 , 4]

sor = []

for i in range(len(li)):
    n = min(li)
    sor.append(n)
    li.remove(n)

print(sor)