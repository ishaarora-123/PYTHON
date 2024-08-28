prizes = int(input("Enter the number of prizes: "))
students = int(input("Enter the number of students:"))
print("The number of prize for each student are: " ,(prizes//students))
print("The number of prizes left are: ",prizes%students)
