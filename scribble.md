🎯 Your first practice

Before we go further, create a small Python file and try these without looking back at the answers:

Exercise 1

Create a list containing 5 numbers and print the first, third, and last elements.

Exercise 2

Create:

[10, 20, 30]

Change 20 to 25.

Exercise 3

Start with:

names = ["Alice", "Bob"]

Add "Charlie" to the end.

Exercise 4

Start with:

numbers = [10, 20, 30, 40]

Remove 30.

Exercise 5 ⭐

Given:

numbers = [10, 20, 30, 40, 50]

use a for loop to print every element.



-------------------------------------------------------------



Your first practice

Try these yourself:

1. Create a tuple containing 5 numbers and print the second and last elements.

2. Try changing one element of the tuple. Observe the error.

3. Loop through a tuple and print every element.

4. Create:

person = ("Sarbesh", 24, "Developer")

Then unpack it into three variables:

name, age, profession = person

and print them.




-------------------------------------------------------------------------





note- 

NOT vs !=


not vs !=
!= — Not Equal

Compares two values.

x != 5

Means:

Is x not equal to 5?

Examples:

5 != 3      # True
5 != 5      # False
not — Logical NOT

Reverses a Boolean result.

not True    # False
not False   # True

Example:

not (x == 5)
x == 5 → True
not True → False

So:

not (x == 5)

is logically equivalent to:

x != 5
Comparison
Operator	Meaning	Purpose
!=	Not equal	Compare two values
not	Reverse/negate	Reverse a Boolean expression
Examples
age != 18

→ age is not 18

not (age >= 18)

→ age >= 18 is false

not True       # False
not False      # True
not (5 > 3)    # False
not (5 == 10)  # True
⭐ Remember
not (x == y)   # equivalent result to
x != y

But not is more general — it can reverse any Boolean expression, while != specifically checks inequality.



-----------------------------------------------------------------------------



Strings quick revision 

🐍 Python Strings — Quick Revision
1. Creating a string
name = "Sarbesh"

A string is a sequence of characters.

S a r b e s h
0 1 2 3 4 5 6
2. Indexing
name[0]      # 'S'
name[2]      # 'r'
name[-1]     # 'h'

Same idea as Lists.

3. Slicing ⭐
name[1:4]

→ characters at indexes 1, 2, 3.

Start included, stop excluded.

name[:4]     # beginning → index 3
name[2:]     # index 2 → end
name[::-1]   # reverse
4. Strings are immutable ⭐

You cannot modify individual characters:

name[0] = "X"   # ❌ Error

Instead, create a new string:

name = "X" + name[1:]
5. Useful string methods
text.lower()          # lowercase
text.upper()          # uppercase
text.strip()          # removes surrounding whitespace
text.startswith("s")  # starts with s?
text.endswith(".")    # ends with .?
text.replace("a", "b")

Methods generally return a new string; they don't modify the original string.

6. Searching/checking
"py" in "python"

→ True

"z" in "python"

→ False

Very useful for simple membership checks.

7. Splitting ⭐
text = "Python is powerful"

words = text.split()

Result:

["Python", "is", "powerful"]

You now have a list of strings.

You can also specify a separator:

data = "Alice,Bob,Charlie"

data.split(",")

→

["Alice", "Bob", "Charlie"]

Very common when processing text/data.

8. Joining ⭐

The opposite of split():

words = ["Python", "is", "powerful"]

" ".join(words)

→

"Python is powerful"

Think:

split() → String → List
join()  → List → String
9. Looping through a string
for char in "Python":
    print(char)

Gives:

P
y
t
h
o
n

Because a string is iterable.

10. len()
len("Python")

→ 6

Just like with lists.

🧠 The String mental model

Remember these:

String
 ↓
Sequence of characters
 ↓
Indexable
 ↓
Sliceable
 ↓
Iterable
 ↓
Immutable

And the high-value methods:

.lower() / .upper()
.strip()
.startswith() / .endswith()
.replace()
.split()
.join()


--------------------------------------------------------------------------------------------------



Strings Recap 



Strings — practical recap

A Python string is a sequence of characters:

text = "Hello Python"

Strings are:

ordered
indexable
sliceable
iterable
immutable
1. Indexing
text = "Python"

print(text[0])   # P
print(text[2])   # t
print(text[-1])  # n

Remember: indexing starts at 0.

2. Slicing
text = "Python"

print(text[0:3])   # Pyt
print(text[:3])    # Pyt
print(text[3:])    # hon
print(text[::-1])  # nohtyP

Pattern:

text[start:stop:step]

stop is excluded.

3. split() — VERY important

This is exactly what we need for our file.

data = "10,20,30,40,50"

numbers = data.split(",")

Result:

['10', '20', '30', '40', '50']
What does split() actually do?

It takes one string and breaks it into a list of strings based on a separator.

"10,20,30".split(",")

means:

Find ,
split there

Result:

["10", "20", "30"]

Another example:

sentence = "Python is easy"

words = sentence.split()
print(words)

Output:

['Python', 'is', 'easy']

When you don't provide anything to split(), Python splits on whitespace.

Important

split() does not convert the values into numbers.

"10,20,30".split(",")

gives:

['10', '20', '30']

not:

[10, 20, 30]

That's why we previously needed:

numbers = [int(number) for number in data.split(",")]
4. join() — opposite of split()

If split() is:

string → list

then join() is:

list → string

Example:

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)

Result:

Python is easy

You can use different separators:

",".join(["10", "20", "30"])

Result:

10,20,30

So remember:

split() → break string apart
join()  → combine strings

These two are very important for file handling, CSV data, APIs, and text processing.

5. strip()

Removes whitespace from the beginning and end.

text = "   hello   "

print(text.strip())

Result:

hello

Very useful when reading files because file data can contain spaces/newlines.

You also have:

text.lstrip()   # left side
text.rstrip()   # right side

You don't need to memorize those yet.

6. replace()

Replace part of a string:

text = "I like Java"

text = text.replace("Java", "Python")

print(text)

Result:

I like Python

Useful for cleaning/modifying text.

7. lower() / upper()
text = "Python"

print(text.lower())  # python
print(text.upper())  # PYTHON

Very useful when comparing user input:

answer = input("Continue? ")

if answer.lower() == "yes":
    print("Continuing...")

Now YES, Yes, yes, etc. can all be handled.

8. Membership: in

You already learned this:

text = "Python programming"

print("Python" in text)

Result:

True

Very useful for checking whether something exists inside a string.

9. startswith() / endswith()
filename = "report.csv"

print(filename.endswith(".csv"))

Result:

True

And:

name = "Sarbesh"

print(name.startswith("S"))

Result:

True

Very useful for filenames, URLs, prefixes, etc.

The ones I want you to remember

Don't try to memorize 30 string methods.

For your goals, these are the high-value ones:

Operation	Purpose
len()	Get length
[index]	Access character
[start:stop]	Slice
.lower()	Convert to lowercase
.upper()	Convert to uppercase
.strip()	Remove surrounding whitespace
.split()	String → list
.join()	List of strings → string
.replace()	Replace text
in	Check whether text exists
.startswith()	Check beginning
.endswith()	Check ending
And this is particularly important for what we're doing now:
"10,20,30,40"
       ↓
    split(",")
       ↓
["10", "20", "30", "40"]
       ↓
     int()
       ↓
[10, 20, 30, 40]

That's the string → parsed data pipeline you'll encounter constantly in Python.

Now we're ready to continue File Handling with writing and appending, and later we'll connect this to CSV/JSON, where these same concepts become even more useful.




------------------------------------------------------------------------------




For your goals, I'd estimate:

CSV: ~30–45 minutes
JSON: ~45–60 minutes
Practice combining them with Python: ~30–45 minutes

So roughly 2–2.5 hours total to get comfortable with the practical fundamentals.

What we'll actually cover

CSV

What CSV is and why it's used
Reading CSV
Writing CSV
Rows/columns
csv module
Converting CSV data into lists/dictionaries
One practical exercise

JSON

What JSON is
JSON objects ↔ Python dictionaries
JSON arrays ↔ Python lists
Reading JSON files
Writing JSON files
Nested JSON
json module
One practical API-style exercise

I wouldn't spend days on CSV/JSON. You need to understand how to move data between files and Python, not become a CSV/JSON specialist.

And after these, I'd consider your basic File Handling section complete and move toward Modules & Packages / Imports, then eventually APIs, SQL/Pandas, etc.





For a SWE interview, yes—but not equally.

JSON → Yes, definitely

You should know basic JSON for SWE/backend interviews.

You should be comfortable with:

import json

with open("data.json", "r") as file:
    data = json.load(file)

and understand:

JSON object  → Python dict
JSON array   → Python list

Why? Because APIs, configuration, web services, and many backend systems use JSON constantly.

Priority: ⭐⭐⭐⭐⭐

CSV → Useful, but lower priority

CSV is more important for Data Engineering / Data Analyst / Data Science than general SWE.

For SWE, knowing how to:

read a CSV
understand rows/columns
parse basic CSV data

is enough initially.

You don't need to memorize the entire csv module.

Priority: ⭐⭐⭐

For your particular goals

Since you're targeting SWE + backend/data-oriented roles, I'd recommend:

JSON       → Learn properly
CSV        → Learn the practical basics

And don't spend 2–3 days on either. We can get the interview-relevant fundamentals done in ~1–2 hours, then move on to higher-ROI topics.

So yes, let's learn them—but don't over-invest in them.



----------------------------------------------------------------



Next: OOP

We'll focus only on what is actually useful for SWE:

What is a class and why do we need one?
Objects
__init__
self — this is the important Python-specific part
Instance variables
Methods
Class vs object
Inheritance
Method overriding
Encapsulation
A little about @classmethod / @staticmethod
Practical exercise

And I'll teach it with context + actual code, rather than just definitions.

After OOP, we'll move into more SWE-useful Python:

Comprehensions → useful built-ins (enumerate, zip, sorted, etc.) → JSON/APIs → testing/debugging → Python interview patterns.

Let's start with classes and objects.



--------------------------------------------------------------------