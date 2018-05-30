size = [5 , 7 , 300 , 90 , 24 , 50 , 75]

print("Hello , my name is Hoang these are my ship sizes")
print(size)
print()

ma = size[0]
for i in range(len(size) - 1):
    if ma < size[i + 1]:
        ma = size[i + 1]
print("Biggest sheep has size '" , ma , "' let's shear it")
print()

for i in range(len(size)):
    if ma == size[i]:
        size[i] = 8
print("After shearing")
print(size)
print()

# for i in range(len(size)):
#     size[i] = size[i] + 50
# print("One month has passed")
# print(size)

n = int(input("Enter number month:"))
for i in range(n):
    ma1 = size[0]
    print("Month" , i + 1)
    total = 0
    for j in range(len(size)):
        size[j] = size[j] + 50
        total += size[j]
    print("One month has passed")
    print(size)

    for j in range(len(size) - 1):
        if ma1 < size[j + 1]:
            ma1 = size[j + 1]
    print("Biggest sheep has size '" , ma1 , "' let's shear it")

    for j in range(len(size)):
        if ma1 == size[j]:
            size[j] = 8
    print("After shearing")
    print(size)

    print("My flock has size in total:" , total)
    print("I would get" , total , " * 2" , " = " , total * 2)
    print()