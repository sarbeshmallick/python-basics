

# Take 2 integers a and b as input
# Find and print the first number btw 1 and 1000 that is divisible by both nos 



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


for i in range(1,1001):
  if (i % a == 0) and (i % b == 0):
    print("The first no to be divisible by both" , i)
    break
    



# Output- 

# Enter first number: 4
# Enter second number: 5
# The first no to be divisible by both 20



# Enter first number: 4
# Enter second number: 6
# The first no to be divisible by both 12



