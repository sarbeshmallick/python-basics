


# Probelem stat-
# Asks the user for two numbers.
# Divides the first number by the second.
# Handles:
# non-numeric input with ValueError
# division by zero with ZeroDivisionError


try:
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  result = a/b
  print(result)


except ValueError:
  print("Enter a valid number")


except ZeroDivisionError:
  print("Cannot divide by zero")