stri = input("Enter your letter : ")
counts = {}

char = list(stri)
chars = sorted(char)
print(chars)
for i in range(len(chars) - 1):
    count = 1
    for j in range(i + 1 , len(chars)):
        if chars[i] == chars[j]:
            count += 1

    if chars[i] not in counts:
        counts[chars[i]] = count

for k in counts:
    print(k , " : " , counts[k] , " times")