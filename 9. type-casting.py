
# Type conversion or Type Casting 

age = input("Enter your age: ")

print (type(age))
print (age)


# print (age + 1)   // we cannot do this as age varibale value i.e 23 is passed as string 

# for solution refer  10. type_conversion-demo



# Output-
# Enter your age: 
# Input - 23
#Output- 
# <class 'str'>
# 23


# see the age varibale is passed as string and not integer although 23 is an integer 
# if we have to do print (age + 1)  we cannot do that 
# it will show TypeError: can only concatenate str (not "int") to str