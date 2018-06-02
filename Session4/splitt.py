n = input("Nhap day so cach nhau boi ' ': ")
 
w = n.strip().split(" ")

numb = []

for item in w:
    numb.append(int(item))

print(numb)

is_sorted = True

for i in range(len(numb) - 1):
    if numb[i] > numb[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("day da sap xep")
else:
    print("day chua sap xep")

    sor = []
    for i in range(len(numb)):
        n = min(numb)
        sor.append(n)
        numb.remove(n)
    print(sor)