n = int(input("Nhap 1 so: "))
is_prime = True

for i in range(2 , n-1):
    if n % i == 0:
        is_prime = False
        break

if is_prime == True:
    print("{0} la so nguyen to".format(n))
else:
    print("{0} khong phai so nguyen to".format(n))