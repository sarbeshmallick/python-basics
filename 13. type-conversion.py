
print (1 + 1.5)

# the above code is implicit is automatically converted by python intepreter, 1 (int) is converted into 1.0(float)



print (1 + int(1.5))                           # this is type casting 

# here in the above code we forced (type casting) 1.5 to become int and it got casted into 1 , so 1 + 1 = 2

 
print (1 + 2.9999)                            # Type Conversion  (implicit)
print (1 + int(2.9999))                       # Type Casting     (explicit)






# Output- 
# 2.5
# 2
# 3.9999
# 3
 
