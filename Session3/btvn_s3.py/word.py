from random import choice

word = input("Enter the word you want:  ")

chars = list(word)
print(chars)
chars2 = []

for i in range(len(chars)):
    n = choice(chars)
    chars2.append(n)
print(chars2)

loop = True

while loop:
    word2 = input("Enter the word you want:  ")

    if word2 == word:
        print("Hura")
        loop = False
    else:
        print("((:")