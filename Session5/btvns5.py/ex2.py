numb = [1, 6, 8 ,1 ,2 ,1 ,5 ,6]

count = 0
n = int(input("enter a number:"))
for i in range(len(numb)):
    if numb[i] == n:
        count += 1

print(n , "appears" , count , "times in my list")