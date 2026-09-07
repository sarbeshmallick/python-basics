

# Given a list of numbers, create a new list containing only the even numbers using a list comprehension.



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_number = []

for number in numbers:
  if number % 2 == 0:
    even_number.append(number)

print(even_number)


