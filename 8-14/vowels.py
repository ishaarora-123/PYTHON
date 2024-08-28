s = input("Enter the string: ")
words = s.split()
c = 0
vowels = ['a','e','i','o','u','A','E','I','O','U']
for i in words:
    for j in i:
        if (j in vowels):
            c = c + 1
print(c)
