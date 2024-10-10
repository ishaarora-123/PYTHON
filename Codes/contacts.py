contacts = [
    ("Isha" , 1234567890),
    ("Isha2" , 234567890),
    ("Isha3" , 34567890),
    ("Isha4" , 4567890),
    ("Isha5" , 567890),
    ("Isha6" , 67890)
]
def add(name, number):
    contacts.append((name, number))
def search(name):
    for i, j in contacts:
        if i == name:
            return j
    return "Not found"
def delete(name):
    for i , j in contacts:
        if (i == name):
            contacts.remove((name, j))
print("What u want to do")
print("1. Adding")
print("2. Search")
print("3. Deleting")
choice = int(input())
if choice == 1:
    print("Enter the name:")
    name = input()
    print("Enter the number:")
    number = int(input())
    add(name, number)
    for i , j in contacts:
        print(i , j)
elif choice == 2:
    print("Enter the name:")
    name = input()
    print(search(name))
else:
    print("Enter the name:")
    name = input()
    delete(name)
    for i , j in contacts:
        print(i , j)