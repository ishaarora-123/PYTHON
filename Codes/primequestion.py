'''list --> check if all the list items are prime in nature
the program must display message correct on the screen
if the list contains non prime numberbut sum of all the elemenst is a prime number
else the system will print incoreect on the screen'''
import math
def isprime(num):
    if (num <= 1):
        return False
    elif (num ==2 or num ==3):
        return True
    else:
        for i in range(2, int(math.sqrt(num))):
            if (num % i == 0):
                return False
    return True
list = []
c = 0
n = int(input("Enter the number of elements in list: "))
for i in range(n):
    num = int(input(i+1))
    list.append(num)
for i in list:
    if (not isprime(i)):
        sum1 = sum(list)
        if(not isprime(sum1)):
            print('Incorrect')
        else:
            print('Correct')
        break
    else:
        c = c + 1
if (len(list) == c):
    print('Correct')
