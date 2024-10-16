import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Teodosija', 'Sutton', 'Taneli', 'Ravshan', 'Ross'],
'Age': [26, 32, 25, 31, 28],
'Salary': [50000, 60000, 45000, 70000, 55000]}

df = pd.DataFrame(data)

# Select rows based on multiple conditions
s_row = df[(df['Name'].str.startswith('T')) |  (df['Age'] > 25)]
print(s_row)


selected_rows = df[(df['Age'] > 25) & (df['Salary'] > 50000)]
print(selected_rows)