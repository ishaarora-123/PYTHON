dic1 = {'a':200, 'b':100, 'e':150}
dic2 = {'a':200, 'b':100, 'f':150}
dic3 = {}
for i in dic1:
    if i in dic2:
        dic3[i] = dic1[i] + dic2[i]
    else:
        dic3[i] = dic1[i] - 50
for i in dic2:
    if i not in dic3:
        dic3[i] = dic2[i] - 50
print(dic3)