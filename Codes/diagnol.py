import numpy as np
def defsum(num):
    sum = 0
    while(num!=0):
        sum = sum + num%10
        num = num / 10
    return sum
def deffact(num):
    pro = 1
    while(num != 0):
        pro = pro * num
        num = num - 1
    return pro
def deftable(num):
    for i in range(11):
        print(i*num)
list1 = []
sum = 0
for i in range(16):
    num = int(input())
    list1.append(num)
arr = np.array(list1)
arr = arr.reshape(4,4)
for i in range(4):
    for j in range(4):
        if i == j or (i+j == 3):
            sum = sum + arr[i,j]
sum1 = sum
digits = 0
flag = 0
for i in range(2,sum):
    if sum%i == 0:
        flag = 1
        break
if flag == 0:
    if sum <= 9:
        print(sum)
    else:
        print(defsum(sum))
else:
    if sum <= 9:
        print(deffact(sum))
    else:
        deftable(sum)