num = int(input("Enter the number: "))
revNum = 0
dupNum = num
sumNum = 0
while(dupNum != 0):
    revNum = 10*revNum + (dupNum%10)
    sumNum = sumNum + dupNum%10
    dupNum = dupNum//10
print(revNum)
print(sumNum)
if (revNum == num):
    print("Palindrome")
else:
    print("Not Palindrome")

