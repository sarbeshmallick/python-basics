

old_age = input("Enter ur age: ")

new_age = int(old_age) + 2

print(new_age)

print (float(new_age))                              # here we converted int to float. It is not conversion but Reassignment 

print (type(new_age))


# Input- Enter ur age: 23

# Output- 
# 25
# 25.0
# <class 'int'>



# if u wondering after converting from int to float why class is int and not float because its a temporaray expression 
# new_age = float(new_age)          // to convert it permanently 



#Useful converion functions
# 1. float()
# 2. bool()
# 3. str()
# 4. int()



# type casting     ->  when coders changes 
# type conversion  ->  python interpreter automatically does it 


# Conversion examples-
# print (1 + 1.5)                // python converts 1 into 1.0 and will give you answer in float (decimal)