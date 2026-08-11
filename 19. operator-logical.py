
# Logical operators 

# these operators work in statement or expression . for eg-   () or ()


# or -> (atleast one statement is true)
# and -> (both are true)
# not -> (reverses any value)


 
stt1 = 3 > 5                                  # False
stt2 = 3 > 2                                  # True 

print (stt1 or stt2)                          # Ans True (cuz one statement stt2 is True )

print ((3 > 5) or (3 > 2))                    # we can write directly also 



print ((3 < 5) and  (3 < 12))                 # Ans True (both the statements are true )



# not operator always does the reverse 

print (not(3 > 2))                            # Ans False , although it is true but as it is not so False 

print (not True)                              # Ans False 

