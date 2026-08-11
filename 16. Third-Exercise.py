
# Problem stat- 
# Take price of 3 products as input (eg - 99.5, 23.75, 16.15)
# print the total Bill amount
# print the average price
# Take a superhero name as input & check if it starts with 'S' / 's' or not.


a = input("Enter price of a: ")
b = input("Enter price of b: ")
c = input("Enter price of c: ")

sum = float(a) + float(b) + float(c)

print(sum)

print(sum / 3 )

print(type(sum))

name = input("Enter your favourite superhero name: ")

print ('S' in name or 's' in name)





# alternatives- 
# Starts with S/s: name.startswith('S') or name.startswith('s')
# Contains S/s anywhere: 'S' in name or 's' in name
# Contains s anywhere, case-insensitive: 's' in name.lower() ← I'd recommend this one