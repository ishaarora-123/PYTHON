num = int(input("Enter the number:"))
if (num == 1 or num == 2):
    print("Prime number")
else:
    for i in range(2,num):
        if (num%i == 0):
            print("Not prime number")
            break
    else:
        print("Prime number")
