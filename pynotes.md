

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
- [12. Mini Project Calculator](#12-mini-project-calculator)
- [13. loops](#13-loops)
- [14. 4th exercise](#14-Multiple-Exercises)
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


Conditional statements allow Python to make decisions.
1. if
2. elif
3. else




#### example code1- 

```
age = 24 

if age >= 18:                                  # in cpp we use {} where if statement is true execute everything inside it. in py it is :
    print("you are adult")                      # 4 spaces . this is called identation which is proper spacing 
    print("you can vote")

elif age < 18:                                  # elif is else if . after if everything we can write in elif 
    print ("you can't vote / drive")

```

>output
you are an adult
you can vote 




#### example code 2- 

Problm stat- Marks are given out of 100. Assign a grade based on the marks:
80–100 → A
60–80 → B
60 → C
write a Python program using if, elif, and else to determine and print the grade.


```
marks = int(input("Enter marks: "))

if marks >= 80:
    print('A')

elif marks >= 60:
    print('B')

else:
    print('C')

```




> If you want to explicitly add into a range then follow this-

if marks >= 60 and marks <= 80:
    print("B")

- marks should be greater than or equal to 60 AND less than or equal to 80.


**Cleaner way-**
if 60 <= marks <= 80:
    print("B")





#### few more examples combing if/esle with operators

1. 
age = 25 

if age >= 18 and age <= 60: 
    print("Eligible")



2. 
name = input("Enter name: ") 

if "S" in name or "s" in name: 
    print("S exists") 
else: 
    print("S does not exist")



This combines:
in → membership operator
or → logical operator
if/else → conditional statement







----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







# 12-mini-project-calculator

Problem stat- 
<!-- # Build a calculator that can perform the following operations:

# a + b
# a - b
# a * b
# a % b
# a ** b -->


```
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Enter operator (+, -, *, /, %, **): ")


if op == '+':
    print("Result:" , a+b)


elif op == '-':
    print("Result:" , a-b)


elif op == '*':
    print("Result:" , a*b)


elif op == '/':
    print("Result:" , a/b)


elif op == '%':
    print("Result:" , a%b)


elif op == '**':
    print("Result:" , a**b )


else:
    print("INVALID OPERATION")

```





--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# 13-loops 




## Range 

- range() function returns a range object that is a sequence of numbers.   starts from 0 



#### Structure for Range

range(start, stop, step)

range (start=0, stop, step=1)                            // default value if nothing specified. but we have to write a stop value everywhere 



> Example 1- 

num = range(5)                           
print(num)                                      // 0,1,2,3,4


> Example 2-
num = range(2, 6)
print(num)                                    // 2,3,4,5


> Example 3-

num = range(10, 0, -2)
print(num)                                   // 10, 8, 6, 4 , 2



> we use range in loops like
for i in range(5):
    print(i)



----------------------------------------------------





## while loop 


> Example 1

counter = 1
while counter <= 5:
    print("Sarbesh win")
    counter = counter + 1

> Output:
Sarbesh win
Sarbesh win
Sarbesh win
Sarbesh win
Sarbesh win




> Example 2

counter = 1                                               //  for counter we give variable name as i 
while counter <= 5:
    print(counter)
    counter = counter + 1


>Output:
1
2
3
4
5





> Example 3

i = 0

while i < 5:
    print(i)
    i = i + 1


> Output:
0
1
2
3
4




- if we encounter infinite loop just press Ctrl + C to stop it




> production

- A while loop is useful when you don't necessarily know beforehand how many iterations you'll need.
  
```
password = ""

while password != "python123":
    password = input("Enter password: ")

```

- Here we don't say: Run this 5 times.
- Instead: Keep running while the condition is true.
  
- for loop -> Iterate over a known sequence/range.
- while loop -> Continue until some condition changes.




> Danger of while loop

```
i = 0

while i < 5:
    print(i)

```

- This never changes i.
- So
    i = 0
    0 < 5 → True
    print
    0 < 5 → True
    print
    0 < 5 → True
    print

- That's an infinite loop.

- we normally need state change
  
  i = 0
while i < 5:
    print(i)
    i = i + 1




>>>  Example 1 of pattern printing using while

i = 1
while i <= 5:
    print(i * '*')
    i = i + 1


> Output
*
**
***
****
*****


### Explaination- 
whenever an integer number is multiplied by a string, that no of times the strings gets repeated.  Multiplication * here is used as concatenation 


>>> like for eg
i = 1
while i <= 5:
    print(i * 'hello')
    i = i + 1

> Output:
hello
hellohello
hellohellohello
hellohellohellohello
hellohellohellohellohello





>>> Reverse pattern printing using while 

i = 5
while i > 0:
    print(i * '*')
    i = i - 1


> Output
*****
****
***
**
*






----------------------------------------------------------------------





## for loop 



> Example 1

for i in range(5):
    print(i)


> Output:
0
1
2
3
4




>>> Another example

nums = range(5)

for i in nums:
  print(i)


> Output
0
1
2
3
4





> Example 2

for i in range(2,6):
    print(i)

> Output:
2
3
4
5



- if its
   i in range(2,6,2):
   print(i)                            // 2 4 

- if its 
    i in range(2,6,5)
    print(i)                           // 2







> Example 3: Another way of finding even numbers 

for i in range(2, 11, 2):         
      print(i)

> Output:
2
4
6
8
10





> Example 4: Cleaner approach for finding even numbers 

for i in range(1, 11):                                                        // to check even no 
    if i % 2 == 0:
        print(i)

> Output:
2
4
6
8
10
  


>>> Example 5: printing multiples of 3 from (1 to 30)

for i in range(1,31):
  if i % 3 == 0:
    print(i)


> Output
3
6
9
12
15
18
21
24
27
30




#### Default structure of range 

range (start, stop, step )
range (optional, must, optional)
range (0,must,0)






#### Concept of for loop 

in c++ we use for loops like this

for (int i = 0; i < 5; i++) {
    cout << i;
}


Python doesn't require you to manually write:
- initialization
- condition
- increment


Instead
for i in range(5):

means   "Take each value produced by range(5) and assign it to i, one at a time."



> for loop dosen't require range() always 

- Python's for loop can directly iterate over collections.

```

names = ["Sarbesh", "Rahul", "Amit"]

for name in names:
    print(name)

```

> Output
Sarbesh
Rahul
Amit



> Why this matters in production

Imagine you're processing data from an API:

```
users = get_users()

for user in users:
    process_user(user)

```

You don't care whether there are 10 users or 10,000 users.






-------------------------------------------------------------------





## break 

- It means Immediately terminate the current loop.


> Example 1

for i in range(10):
    if i == 5:
        break

    print(i)


> Output
0
1
2
3
4


- when i == 5 becomes true , Python executes break.  The Loop ends immediately 




>>> Example 2: printing multiples of 3 from (1 to 30) but stop when number reaches 21 

for i in range(1,31):
  if i == 21:
    break
  if i % 3 == 0:
    print(i)

print("out of loop")


> Output
3
6
9
12
15
18
out of loop 






> Production : when break is uselful?

Imagine searching for something:

numbers = [4, 7, 2, 9, 15, 3]

for number in numbers:
    if number == 9:
        print("Found!")
        break

- Once you've found what you're looking for, there's no reason to continue searching.






---------------------------------------------------------------------





## continue 

- It means Stop the current iteration right here and immediately move to the next iteration. 
- skiping some particular iteration 


> example 1

for i in range(1, 6):

    if i == 3:
        continue

    print(i)


> Output
1
2
4
5


> Trace:

**Iteration 1**
i = 1
i == 3? No
print(1)


**Iteration 2**
i = 2
i == 3? No
print(2)


**Iteration 3**
i = 3
i == 3? Yes
continue                         // python dosent execute print(i)  .   It jumps back to the loop and starts the next iteration.


**Iteration 4**
i = 4
print(4)


**Iteration 5**
i = 5
print(5)




> Remember

break
  ↓
EXIT LOOP COMPLETELY


continue
  ↓
SKIP THIS ITERATION
  ↓
NEXT ITERATION




> Production : A realistic use of continue 

Suppose you're processing numbers and only want to work with positive numbers:

```
numbers = [10, -5, 20, -3, 30]

for number in numbers:

    if number < 0:
        continue

    print(number)

```

> Output
10
20
30


- here continue means Negative numbers aren't relevant to this processing, so skip them.  Filtering Logic 





>>> Example: printing multiples of 3 from (1 to 30) but skip the number 21 

for i in range(1,31):
  if (i == 21):
    continue
  if (i % 3 == 0):
    print(i)


> Output
3
6
9
12
15
18
24
27
30






----------------------------------------------------------------------------






## Nested loop

- A loop inside another loop 



>>> Example

for i in range(3):
    for j in range(3):
        print(i, j)


> trace:

Outer loop starts: i = 0
Inner loop:
j = 0 → print(0, 0)
j = 1 → print(0, 1)
j = 2 → print(0, 2)


Outer loop: i = 1
Inner loop starts again from begining 
j = 0 → print(1, 0)
j = 1 → print(1, 1)
j = 2 → print(1, 2)


Outer loop: i = 2
and again inner loop:
j = 0
j = 1
j = 2


> Output:
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2



#### Mental model
The inner loop completes all its iterations for every single iteration of the outer loop.



#### Why nested loops matter for interviews?


Suppose:

for i in range(n):
    for j in range(n):
        print(i, j)


- The outer loop runs n times.
- For each outer iteration, the inner loop runs n times.
- therefore, n × n = n²
- time complexity ->  O(n²)


You'll encounter them in:
matrix problems
2D arrays
brute-force solutions
pair comparisons
sorting algorithms
graph algorithms
pattern problems





#### nested loops + break

Consider:

for i in range(3):

    for j in range(5):

        if j == 2:
            break

        print(i, j)


- break breaks the inner loop only and not outer loop 

for i = 0
inner loop:
j = 0 → print
j = 1 → print
j = 2 → break


> Output
0 0
0 1
1 0
1 1
2 0
2 1







----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 






# 14-multiple-exercises


1. Problem stat- Print all odd numbers from 1 to 20 

```
for i in range(1,21):
  if (i % 2 != 0):
    print(i)

```

> Output
1
3
5
7
9
11
13
15
17
19



#### ALternative way 

for i in range(1,21,2):
    print(i)



------------------------------------------------



2. Problem stat- Print the table of 57

```
for i in range(1,11):
  print(57 * i)

```

> Output
57
114
171
228
285
342
399
456
513
570



#### refined way 

```
for i in range(1, 11):
    print(57, "x", i, "=", 57 * i)

```

> Result:
57 x 1 = 57
57 x 2 = 114
57 x 3 = 171
.. .. .... 




#### same thing with while loop 

```
i = 1

while i <= 10:
    print(57 * i)
    i = i + 1

```


#### Alt way of writing in while 

```
i = 1

while i in range(1, 11):
    print(57 * i)
    i = i + 1

```


- while expects condition in True or False  unlike for loop but this thing can also work 
- but in real production code, you would usually use while with a condition that expresses the actual stopping rule rather than i in range(...).



#### Real usage of while 

while password != correct_password:
    password = input("Enter password: ")


while not connected:
    connect_to_server()


while queue:
    item = queue.pop(0)
    process(item)



for → "Go through these things / repeat this known number of times."
while → "Keep doing this until this condition changes."






--------------------------------------------------------------------




3. Problem stat- Print all multiples of 3 from 1 to 50 but skip 15 

```
for i in range(1,51):
  if (i == 15):
    continue 
  if (i % 3 == 0):
    print(i)

```

> Output
3
6
9
12
18
21
24
27
30
33
36
39
42
45
48



--------------------------------------------------------------------




4. Take two integers a and b as input. Find and print the first number between 1 and 1000 that is divisible by both numbers.


```


























