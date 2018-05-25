height = int(input("nhap chieu cao:  "))
weight = int(input("nhap can nang:  "))
h = height * height / 10000
bmi = weight / h
if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")