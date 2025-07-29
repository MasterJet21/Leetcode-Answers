# Python code demonstrate creating 
# DataFrame from dict narray / lists 
# By default addresses.
 
# # intialise data of lists.
# data = {'Name':['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
#         'Salary':[4548, 28150, 1103, 6593, 74576, 24433]}
 
# # Create DataFrame
# df = pd.DataFrame(data)
 
# # Print the output.
# print(df)

################################################################################################
# Using module
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees_df = pd.DataFrame(employees)
    new_column = []

    for i in employees['Salary']:
        i = i * 2
        new_column.append(i)

    employees_df.insert(2, 'Bonus', new_column)
    print(employees_df)

createBonusColumn({'Name':['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
        'Salary':[4548, 28150, 1103, 6593, 74576, 24433]})

################################################################################################