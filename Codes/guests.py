guests = [
    ("Isha" , 56),
    ("Isha2" , 22),
    ("Isha3" , 35),
    ("Isha4" , 45),
    ("Isha5" , 24),
    ("Isha6" , 38)
]
adult = []
younger = []
for i, j in guests:
    if (j < 30):
        adult.append(i)
    else:
        younger.append(i)
print("Adult: " , adult)
print("Younger: ",younger)