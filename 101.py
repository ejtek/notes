#!/usr/bin/env python

### https://www.youtube.com/watch?v=egg-GoT5iVk&list=PLLKT__MCUeiwBa7d7F_vN1GUwz_2TmVQj&index=2

""" This is a docstring note useful
for documentation, program version, etc """

# Help
help()

# This is a comment

# Print string
print("Strings and things:")
print('Hello world!')
print("""Hi, this is
a multi-line string!""")
print("This is"+" a string")

print('\n')  # new line

# Math
print("Math time:")
print(50 + 50)	# add
print(50 - 50)  # subtract
print(50 * 50)	# multiply
print(50 / 50)  # divide
print(50 + 50 - 50 * 50 / 50)  # PEMDAS
print(50 ** 2)  # exponents (number powered)
print(50 % 6)   # modulo (remainder of operation)
print(50 // 6)  # without decimal
print('\n')  # new line

# Variables and Methods
print("fun with variables and methods:")
quote = "All is fair in love and war"
print(len(quote))  # lengh
print(quote.upper())  # uppercase
print(quote.lower())  # lowercase
print(quote.title())  # title

name = "James"
age = 29	# int int(29)
gpa = 3.7	# float float(3.7)

print(int(age))
print(int(29.9))	# does not round

print("My name is " + name + " and I am " + str(age) + " years old.")

print('\n')		# new line

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')		# new line

# Functions
print("Now, some functions:")


def who_am_i():
    name = "James"
    age = 29
    print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

# Adding parameters

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

# Adding multiple parameters

def add(x, y):
    print(x + y)

add(7, 7)
add(305, 207)

# Using return

def multiply(x, y):
    return x * y

print(multiply(7, 7))

def square_root(x):
    return x ** .5

print(square_root(64))

print('\n')  # new line

# Boolen Expressions (True or False w/ capital letter)
print("Boolean expressions:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

# Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (8 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and, test_or, test_not)

print('\n')  # new line

# Conditional Statements
print("Conditional statements:")

def soda(money):
    if money >= 2:
        return "You've got yourself a soda"
    else:
        return "No soda for you"

print(soda(3))
print(soda(1))

def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "We're getting tipsy!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid."
    else:
        return "You're broke and too young."

print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 4))

print('\n')  # new line

# Lists
print("Lists have brackets:")
movies = ["Wheh Harry Met Sally", "The Hangover",
          "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[0])	# first item
print(movies[0:3])	# range
print(movies[1:])
print(movies[:1])
print(movies[-1])	# last item

movies.append("JAWS")	# adds to end of line
print(movies)

movies.pop()	# removes last item
print(movies)

movies.pop(1)
print(movies)

movies = ["Wheh Harry Met Sally", "the Hangover",
          "The Perks of Being a Wallflower", " The Exorcist"]
person = ["Jake", "James", "Leah", "Jeff"]
combined = zip(movies, person)
print(list(combined))

# Tuples
print("Tuples have parentheses and cannot change:")
grades = ("A", "B", "C", "D", "F")
print(grades[1])

# Sets (always have unique value)
example = {1, 2, 5, 4, 2}
print(example)
{1 ,2, 5, 4}	# removes duplicate value

# Looping
print("For loops - start to finish of iterate:")
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:	# For Loop
    print(x)

print("while loops - Execute as long as True:")
i = 1
while i <= 10:	# While Loop
    print(i)
    i += 1
