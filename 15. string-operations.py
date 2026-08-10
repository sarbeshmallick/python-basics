# shortcut command for commenting  ->   Select and Ctrl + /
# string operations 


name = "Sarbesh Mallick "

print (name)

print (name.upper())

print (name.lower())

print (name)                             # the original value is intact 

# when we do any operations in string it dosen't impact the original value 
# in python strings are Immutable 




# find function  
print (name.find('M'))                   # if that string exists then we will get the index of that thing 


# find function returns index which is position
# if we search something that is not present we will get -1 as value which is invalid 




# replace method  

print (name.replace("Sarbesh Mallick" , "Muthu"))
print (name.replace("Mallick" , "Muthu"))                           # when we need to replace smthng partial 
print (name.replace("S" , "D"))




# check function 

print ('S' in name)                                      # in is a keyword which checks presence and results comes in True or False 

# in is a keyword in python dictionary, we cannot use in as a varibale name, in operator  job is to search 
# in is not a function but a operator. 
# in()       # ❌
# print()    # function ✅



# A useful rule for your notes:

# Functions → generally called independently: print(), input(), int()
# Methods → called using . on an object: "hello".upper(), "hello".replace()
# So if your course asks "Is replace a function?", technically: str.replace() is a method, not a standalone function.







