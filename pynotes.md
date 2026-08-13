

# Weclome to Learning Python with me 


## Table of Contents
- [1. Basics](#1-basics)
- [2. Variables](#2-variables)
- [3. Data Types](#3-data-types)
- [4. Input](#4-input)
- [5. 1st Exercise](#5-First-Exercise)
- [6. Type Casting/Conversion](#6-Type-Casting-or-Type-Conversion)
- [7. 2nd Exercise](#7-Second-Exercise)
- [8. String Operations](#8-string-operations)
- [9. 3rd Exercise](#9-Third-Exercise)
- [10. Operators](#10-Operator)
- [11. Condition if/else statements](#11-Conditional-statements) 
- 



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# 1-basics 

Python is case-sensitive.

print("Hello World")

print() is used to display output.  like print("Tea")   or   print(10)


print("Hello", "World")                        // Multiple values can be printed together.



> **Comments**
Use # for comments

and to selected multiple block of code just click Ctrl + /


> in terminal to use the previous command just press upwards arrow (↑)


- python is case senstive meaning print() will work but not Print()





------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# 2-variables 


A variable stores a value.

> For ex
name = "Sarbesh"
age = 26
cgpa = 8.5


> Here:
name → variable
"Sarbesh" → value
= → assignment operator

The assignment operator stores the value on the right-hand side in the variable on the left-hand side.

```
**Variables can be updated and the new variable will get printed **
age = 26
age = 25.5

print(age)
```

> Output:
25.5

- to print varibales just type print(variable name)  and no need of " " even its a string 


### varibale code- 
```
name = "Sarbesh"

first_name = "Sarbesh"
last_name = "Mallick"
age = 26 
gender = "male"
eye = "brown"
age = 100


print(first_name)
print(age)

print(gender , eye)

print(30)
```

>Output- 
Sarbesh
100
male brown
30 




--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# 3-data-types


Python hv 4 primitive data types


| Type    | Meaning                | Example          |
| ------- | ---------------------- | ---------------- |
| str     | String / text          | "Sarbesh"        |
| int     | Integer / whole number | 25               |
| float   | Decimal number         | 8.5              |
| bool    | Boolean                | True / False     |



> Examples:

name = "Sarbesh"       # str
age = 25               # int
cgpa = 8.5             # float
isStudent = True       # bool


Boolean values must use capital letters:
True
False

Not: true and false. Python is case-sensitive.



### Checking the data type-


**Use the built-in type() function:**


### type check code-
```
name = "Sarbesh"
age = 26
balance = 0.5 
gender = "Male"


print (type(name))

print (type(age))

print (type(balance))
```

> Output-
<class 'str'> 
<class 'int'> 
<class 'float'>


- type() tells us what type of value a variable currently contains.
- in c++ we need to define our variable values like for numbers int num = 5; but in python we can just declare it as it is without typing int
- to check what the type is we do print(type(variable name))





---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# 4-input 


**Use input() to take input from the user.**


name = input("Enter your name: ") 
print(name)



### Eg code-
```
name = input("What is ur name: ")
profession = input(" what is ur job: ")
age = input("what is ur age: ")

print(name)
print(profession)
print(age)
```

> Input
What is ur name: Sarbesh
what is ur job: Dev
what is ur age: 16

>Output 
Sarbesh
Dev
16



### 6. Input code- 
```
name = input("Enter your name: ")

print("Namaste" , name)
```

> Input
Enter your name: Sarbesh

>Output- 
Hello Namaste Sarbesh



### Tip- 

suppose my python filename is 6. Input.py 

- if we run this program using python filename.py then remember as I have used spaces to use " "  in terminal 
- like for example-
    python "6. Input.py"



### Important- 

input() always returns a string.

Even if the user enters: 23
Python initially stores it as:  "23"   
not: 23

input returns a string even it is a number(int) 



--------------------------------------------------------



## Concatenation

concatenation means joining strings.

+ 


> for eg:

name = "Sarbesh"
print("Hello " + name)

>Output-
Hello Sarbesh 


> Remember
Be careful about spaces:

"Hello" + name 
produces:
HelloSarbesh


"Hello " + name
produces:
Hello Sarbesh


- The + operator can concatenate strings.




### 7. concatenation code-
```
name = input("Enter your name: ")

print("Hello Namaste " + name)
```

> Input
Enter your name: Sarbesh

> Output-
Hello Namaste Sarbesh






-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# 5-First-Exercise 


Problem stat-
<!-- # Add a person with first name as Tony and last name as Stark.
# Tony's age is 53.
# Tony's height is 1.85m.
# Tony is secretly a superhero. Take his superhero name as input & print it. --> 


```
first_name = "Tony"
last_name = "Stark"

age = 53
height = 1.85 

name = input("What is his superhero name: ")
print(name)
```

> Input 
What is his superhero name: Ironman

>Output 
Ironman 




-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# 6-Type-Casting-or-Type-Conversion


Because input() returns a string, we often need to convert it before performing calculations.

type casting     ->  when coders changes 
type conversion  ->  python interpreter automatically does it 


> Common conversion functions:
int()
float()
str()
bool()


### type casting code- 
```
age = input("Enter your age: ")

print (type(age))

print (age)
```

> Input
Enter your age: 23

> Output
<class 'str'>
23


> Note-
-  print (age + 1) ❌                                                                       // we cannot do this as age varibale value i.e 23 is passed as string 
-  see the age varibale is passed as string and not integer although 23 is an integer 
-  if we have to do print (age + 1)  we cannot do that 
-  it will show TypeError: can only concatenate str (not "int") to str



### Solution for this 

```
age = input("Enter your age: ")

age = int(age)

print (type(age))

print (age)
print (age + 1)
```

> Input- Enter your age: 23

> Output
<class 'int'>
23
24


- Now age is an integer 




---------------------------------------------------




## Temporary Conversion vs Reassignment 


Let's understand this with code-

```
old_age = input("Enter ur age: ")

new_age = int(old_age) + 2

print(new_age)

print (float(new_age))                              # here we converted int to float. It is not conversion but Reassignment 

print (type(new_age))
```


> Input- 
Enter ur age: 23

> Output- 
25
25.0
<class 'int'>


> Note-
- if u wondering after converting from int to float why class is int and not float because its a temporaray expression 
- new_age = float(new_age)            // to convert it permanently 


type casting     ->  when coders changes 
type conversion  ->  python interpreter automatically does it 


Conversion examples-
print (1 + 1.5)                // python converts 1 into 1.0 and will give you answer in float (decimal)




### Temporary Conversion-

age = 23

print(float(age))
print(type(age))

> Output:
23.0
<class 'str'>

- float(age) converted the value for that expression, but age itself remained a string.



### Permanent conversion / reassignment- 

age = 23

age = float(age) 

print(age)
print(type(age))


> Output
23
<class 'float'>


- The converted value was assigned back to age.



### Easy rule

float(age)
→ temporary conversion
- onverts the value for that expression; original variable remains unchanged.

age = float(age)
→ conversion + reassignment
- converts the value and stores the converted value back in the variable.


You do not always need a new variable.

> For example:

print(float(age) + 1.2)

is perfectly valid when you only need the converted value temporarily.





### Another code eg-

```
age = input("enter age: ")

print(float(age) + 1.2)

print(type(age))
```

> Input
enter age: 23

> Output
24.2
<class 'str>


Temp conversion-
print(float(age))                // age is still a string 
 
Permanent Conversion- 
age = float(age)                // age is now float 





-------------------------------------------------------------





# Explicit vs Implicit Conversion 



**Implicit Conversion-**

Python automatically performs a compatible conversion.


> Example:

print(1 + 1.5)

> Result:
2.5

- the above code is implicit is automatically converted by python intepreter, 1 (int) is converted into 1.0(float)
- Python promotes the integer to a float during the operation.





**Explicit Conversion / Type Casting-**

The programmer tells Python to convert the type.


> example:

print(1 + int(2.9999))

// Python is explicitly told to convert 2.9999 to an integer.

> Result:
3



> another example:
print (1 + int(1.5))            

- this is type casting
- here in the above code we forced (type casting) 1.5 to become int and it got casted into 1 , so 1 + 1 = 2
- Result: 2


> Summary

print (1 + 2.9999)                             // Type Conversion  (implicit)              // Result: 3.9999
print (1 + int(2.9999))                        // Type Casting     (explicit)              // Result: 3





--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# 7-Second-Exercise 


Problem stat- Sum Program where a , b integers nos we hv to take input and calc the sum of a & b and print it

```
a = input("Enter first number: ")

b = input("Enter second number: ")

total = int(a) + int(b)

print("the sum is" , total)
```


> Input
Enter first number: 10
Enter second number: 20

> Output
the sum is 30 


> Alt
a = int(input("Enter first number: "))                    
b = int(input("Enter second number: "))
total = (a + b)
print(total)





------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







# 8-string-operations 


- Strings have useful methods 
- Strings are immutable. 
- String operations do not modify the original string rather a new string is produced.



### let's understand from code- 

```
name = "Sarbesh Mallick "

print (name)

print (name.upper())

print (name.lower())

print (name)                                         //  the original value is intact 
```

> Output-
Sarbesh Mallick
SARBESH MALLICK
sarbesh mallick 
Sarbesh mallick                                      //  the original value is intact cuz strings are immutable 





--------------------------------------------




## find() method 


- find() searches for a substring/character and returns its index/position.
- returns no of the index and not boolean (true/false)


> example:

name = "Sarbesh"
print(name.find("b"))

> Output:
3


- If the character exists, Python returns its index.
- If it doesn't exist:
      name.find("z")
      
      returns:
      -1


> Summary:
find() → tells you where something occurs.
It does not simply return True or False.



### Code-

```
name = "Sarbesh Mallick"

print (name.find('M'))                                               // if that string exists then we will get the index of that thing 
```

> Output-
8

> Remember- 
find function returns index which is position
if we search something that is not present we will get -1 as value which is invalid 






## replace() method


replace() is a string method, not a standalone function.


> for eg:

name = "Sarbesh Mallick"
print(name.replace("Mallick", "Muthu"))

> Result:
Sarbesh Muthu


- You call it using .
- variable_name.replace(...)
- .replace()




### example code-

```
name = "Sarbesh Mallick"

print (name.replace("Sarbesh Mallick" , "Muthu"))
print (name.replace("Mallick" , "Muthu"))                           
print (name.replace("S" , "D"))                                         // when we need to replace smthng partial 

```

> Output-
Muthu
Sarbesh Muthu
Darbesh Mallick







## in operator 

- It is a check method. 
- it checks whether something exists or not and results comes in boolean (True/False)


> for eg 1

name = "Sarbesh"
print("S" in name)

> Result: 
True


> for eg 2
numbers = [10, 20, 30]
print(20 in numbers)

> Result:
True



#### not in 

> for eg 3

numbers = [10, 20, 30]
print(40 not in numbers)

> Result:
True


- in is a keyword in python dictionary, we cannot use in as a varibale name, in operator  job is to search 



### Note-

'S' in name
→ checks whether S exists anywhere

**Whereas:**

name.startswith('S')
→ checks whether the string starts with S.



### Function vs Method 

Functions are generally called independently:

print()
input()
int()
float()

Methods are called on an object:

name.upper()
name.lower()
name.replace()


- Functions → generally called independently: print(), input(), int()
- Methods → called using . on an object: "hello".upper(), "hello".replace()






---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# 9-Third Exercise

Problem stat-
<!-- # Problem stat- 
# Take price of 3 products as input (eg - 99.5, 23.75, 16.15)
# print the total Bill amount
# print the average price
# Take a superhero name as input & check if it starts with 'S' / 's' or not. -->


```
first_product = 101.55
second_product = 99.95
third_product = 15.15 


total = int(first_product) + int(second_product) + int(third_product)

print(total)

print ("the average price is: " , total/3)

name = input("What's your supehero name: ")

print (name.startswith('s') or name.startswith('S'))                            // Alt-    print(name.startswith(('s', 'S')))     OR       print(name.lower().startswith('s'))

```


> Output-
215
the average price is:  71.66666666666667
What's your supehero name: Sarbesh
True


- if I want to check if S or s in the whole name is there or not then:
            print ('S' in name or 's' in name)







----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







# 10-Operator 


## Arithmetic Operator 
1. **Arithmetic Operators-** 



| Operator | Name                   | Example  |
| -------- | ---------------------- | -------- |
| +        | Addition               | 5 + 2    |
| -        | Subtraction            | 5 - 2    |
| *        | Multiplication         | 5 * 2    |
| /        | Division               | 5 / 2    |
| //       | Floor Division         | 5 // 2   |
| %        | Modulus / Remainder    | 5 % 2    |
| **       | Exponentiation / Power | 5 ** 2   |



print (5 + 3)                                   //  + is addition operator and 5,3 are operands 
print (5 - 3)
print (5 * 3)
print (5 / 3)                                   //   / is division operator 

print (5 // 3)                                 //    is floor division and completely removes the decimal part, only int part is left 

print (5 % 3)                                  //   % is modulus or remainder , very helpful to check even & odd

print (5 ** 3)                                 //   ** is exponent of or power of 5³   = 5*5*5 = 125 



1. 5/2        -> 2.5
2. 5 // 2     -> 2

    Very useful for checking even/odd:
    number % 2 == 0       → even
    number % 2 != 0       → odd

3. 5 ** 2    -> 25  (5² = 25)




--------------------------------------------------------------





### Operator Precedence

- Python follows operator precedence rules when multiple operators appear in an expression.
- just like in real life BODMAS is followed 
- operator precedence are rules that defines which operator has higher priority compared to other 



> For example:

2 + 5 * 3  
 = 17
Multiplication happens first


**But parentheses have higher priority:**
(2 + 5) * 3
Result: 21



**Basic rule to remember**
1. ()
2. **
3. * / // %
4. + -


- **For operators with the same precedence, evaluation generally proceeds from left to right.**

- **When in doubt, use parentheses to make the intended order clear.**

- if * and / both are present then our operations will start from Left -> Right 

- parantheses() have highest priority. 





-------------------------------------------------------------




## Operator comparison 
2. Operator Comparison 



Comparison operators compare values and produce a Boolean result: TRUE or FALSE 


| Operator | Meaning                  |
| -------- | ------------------------ |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or equal to |
| <=       | Less than or equal to    |
| ==       | Equal to                 |
| !=       | Not equal to             |



> Examples:

3 > 2
True

2 < 5
True

2 == 5
False

2 != 5                                // !=  is NOT operator 
True




### Remember-

= vs ==

= is the assignment operator:
age = 25
It assigns a value.


== is the comparison operator:
age == 25
It checks whether the values are equal.


= → assign
== → compare

This distinction is extremely important in if statements.




------------------------------------------------------





## Logical Operator 
3. Logical Operator 


- Python has three main logical operators:
and
or
not



1. and
Both conditions must be true.
(3 < 5) and (3 < 12)
→ True


> Conceptually:
True AND True → True
True AND False → False
False AND True → False
False AND False → False



2. or 
At least one condition must be true.
(3 > 5) or (3 > 2)
→ True


> Conceptually:
True OR True → True
True OR False → True
False OR True → True
False OR False → False



3. not 
Reverses a Boolean value.

not True
→ False

not False
→ True



- these operators work in statement or expression . for eg-   () or () 
  
or -> (atleast one statement is true)
and -> (both are true)
not -> (reverses any value)


> example

stt1 = 3 > 5                                      //  False
stt2 = 3 > 2                                     // True 

print (stt1 or stt2)                             // Ans True (cuz one statement stt2 is True )

print ((3 > 5) or (3 > 2))                      // we can write directly also 



print ((3 < 5) and  (3 < 12))                   // Ans True (both the statements are true )



# not operator always does the reverse 

print (not(3 > 2))                             //  Ans False , although it is true but as it is not so False 

print (not True)                               // Ans False 








----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------









# 11-Conditional-statements 





























