

# Write a program that asks the user to enter a number and prints: 
# You entered: 25 
# if the input is valid.

# If they enter something like: hello
# it should print:
# Invalid input. Please enter a number.


try:
  number = int(input("Please enter a number: "))
  print("You entered:", number)

except ValueError:
  print("Invalid input. Please enter a number")


