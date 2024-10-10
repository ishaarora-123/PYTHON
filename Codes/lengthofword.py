input_string = input("Enter the string")
n = int(input("Enter the length of the word"))
words = input_string.split()
long_words = [word for word in words if len(word) > n]
print(long_words)
