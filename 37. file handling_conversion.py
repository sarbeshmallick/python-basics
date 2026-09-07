# Created a file called numbers.txt where I stored 10, 20, 30, 40, 50 

# Then created a python file where I wrote the logic to read its contents. So it is   File -> Python 


with open("numbers.txt", "r") as file:
  content = file.read()

numbers = []

for number in content.split(","):
  numbers.append(int(number))


print(numbers)
print(sum(numbers))





