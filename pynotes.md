

# Weclome to Learning Python with me 


## Table of Contents
- [1. Basics](#1-basics)
- [2. Variables](#2-variables)
- [3. Data Types](#3-data-types)
- [4. Input](#4-input)
- [5. Operators](#5-operators)
- [6. if/else](#6-ifelse)
- [7. Practice Exercises](#7-practice-exercises)
- [8. Mini Projects](#8-mini-projects)



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









