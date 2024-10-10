with open ('E:/MCA/MCA 3rd/python/9-27/file1.txt' , 'r') as f:
    count = 0
    for line in f:
        s = line.split(' ')
        for i in s:
            if i == 'hack':
                count = count + 1
print(count)