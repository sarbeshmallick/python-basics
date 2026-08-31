
# problem stat-

# Given a list of roll numbers: [101, 105, 102, 101, 108, 105, 110]. Print all unique roll nums in the list.

# Given Employee records in the form of a list of tuples where each tuple contains:
# (Employee ID, Employee Name, Salary)
# Example - [
#     (101, "Alice", 50000),
#     (102, "Bob", 65000),
#     (103, "Charlie", 45000)
# ]
# Ask user to enter Employee ID & search it inside records.



roll_number = [101, 105, 102, 101, 108, 105, 110]
unique_number = set(roll_number)
print("unique roll numbers" , unique_number)



records = [
  (101, "Alice", 50000),
  (102, "Bob", 65000),
  (103, "Charlie", 45000)
]


employee_id = int(input("Enter your employee id: "))


for record in records:
  if record[0] == employee_id:
      print(record)
      break




# we can use alternatives like else or found variable tp print if user enters wrong employee id 




  















