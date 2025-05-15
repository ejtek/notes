#!/usr/bin/env python

### https://www.youtube.com/watch?v=6VElWbND-zg&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=1

#############
# PYTHON
#############

#print(help(datatype))

### PRINT
#print("I love pizza")
#print("It's really good!")

### VARIABLES = Reusable container for storing a value
### Value behaves as if it were the value it contains
#age = 99
#print(age)
#print("You are", age, "years old")
#print("You are " + str(age) + " years old")
#print(f"You are {age} years old")   # FSTRING is prefered method
#x, y, z = 1, 2, 3
#x = y = z = 1

### DATA TYPES = Integer, Float, String, Boolean
### INTEGER
#players = 2
#quantity = 5
#print(f"There are {players} players online")
#print(f"You would like to buy {quantity} items")

### FLOAT
#gpa = 4.0
#distance = 2.5
#price = 10.99
#print(f"Your gps is {gpa}")
#print(f"You ran {distance}km")
#print(f"The price is ${price}")

### STRING
#name = "Bro"
#food = "pizza"
#print(f"Hello {name}")
#print(f"You like {food}")

### BOOLEAN
#online = True
#for_sale = False
#running = True
#print(f"Are you online? {online}")
#print(f"Is the item for sale? {for_sale}")
#print(f"Game running: {running}")

### TYPECASTING = The process of converting a value of one data type to another
### Explicit vs Implicit
#name = "Bro"
#age = 99
#gpa = 4.0
#student = True
#print(type(name))
#age = float(age)
#gpa = int(gpa)
#student = str(student)
### Converting a number to boolean is always True unless the number is zero
#age = bool(age)
#print(age)

### Implicit = Below example converts to float based on mathematical operation
#x = 2
#y = 2.0
#x = x / y
#print(x)

### USER INPUT
#name = input("Enter your name: ")
#age = input("enter your age: ")
#print(f"Hello {name}")
#print(f"You are {age} years old")

#length = float(input("Enter the length of a rectangle: "))
#width = float(input("Enter the width of a rectangle: "))
#area = length * width
#print(f"The area is {area}cm^2")

### ARITHMETIC OPERATORS
#print(50 + 50)  # add
#print(50 - 50)  # subtract
#print(50 * 50)	# multiply
#print(50 / 50)  # divide
#print(50 + 50 - 50 * 50 / 50)   # PEMDAS
#print(50 ** 2)  # exponents (number powered)
#print(50 % 6)   # modulo (remainder of operation)
#print(50 // 6)  # without decimals

#friends = friends + 1
#friends += 1
#friends = friends - 2
#friends -= 2
#friends = friends * 3#
#friends *= 3
#friends = friends / 2
#friends /= 2
#print(friends)

### BUILT-IN FUNCTIONS
#x = 3.14
#y = 4
#z = 5
#result = round(x)   # round number
#result = abs(y)     # absolute value
#result = pow(4, 3)  # power
#result = max(x, y, z)   # maximum value
#result = min(x, y, z)   # minimum value
#print(result)

### IF ELSE = Execute code only IF condition is True
#age = int(input("Enter your age: "))
#if age >= 18:
#    print("You are eligible")
#elif age <= 0:
#    print("You haven't been born yet!")
#else:
#    print("You must be 18+ to sign up")

### LOGICAL OPERATORS = Used on Conditional statements
### and = checks two or more conditions is True
### or = checks if at least one condition is True
### not = checks if condition is False, and vice versa
#temp = 25
#if temp > 0 and temp < 30:
#    print("The temperature is good")
#else:
#    print("The temperature is bad")

#temp = 40
#if temp <= 0 or temp >= 30:
#    print("The temperature is bad")
#else:
#    print("The temperature is good")

#sunny = True
#if sunny:
#    print("It is sunny outside")
#else:
#    print("It is cloudy outside")

#if not sunny:   # not operator flips the results
#    print("It is sunny outside")
#else:
#    print("It is cloudy outside")

### USEFUL STRING METHODS
#name = input("Enter your name: ")
#result = len(name)
#result = name.find(" ")    # name.rfind(" ") finds occurances in reverse
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()    # returns true only if entire string is integer
#result = name.isalpha()
#print(result)

### INDEXING = Access elements of a sequence using [start : end : step]
#credit_number = "1234-5678-9012-3456"
#print(credit_number[0])
#print(credit_number[:4])
#print(credit_number[5:9])
#print(credit_number[10:])
#print(credit_number[-1])
#print(credit_number[::2])  # every two steps
#print(credit_number[::-1]) # reversed order

### FORMAT SPECIFIERS = {value:flags} format a value based on inserted flags
### .(number).f = round to that many decimal places (fixed point)
### :(number) = allocate that many spaces
### :03 = allocate and zero pad that many spaces
### :< = left justify
### :> = right justify
### :^ = center align
### :+ = use a plus to indicate positive value
### := = place sign to leftmost position
### :  = insert a space before positive numbers
### :, = comma seperator

### WHILE LOOP = Execute code WHILE some condition ramains True
#name = input("Enter your name: ")
#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your name: ")
#print(f"Hello {name}")

### FOR LOOP = Execute a block of code a fixed number of times
### You can iterate over a range, string, sequence, etc
#for x in range(1, 21):
#    print(x)

#for x in range(1, 21):
#    if x ==13:
#        continue    # continue skips and break exits the loop
#    else:
#        print(x)

### NESTED LOOP = A loop within another loop (outer, inner)
#for x in range(3):
#    for y in range (1, 11):
#        print(y, end="")
#    print()

### COLLECTION = Single "variable" used to store multiple values
### LIST = [] ordered and changeable. Duplicates OK
### SET = {} unordered and immutable, but Add/Remove OK. NO duplicates
### TUPLE = () ordered and unchageable. Duplicates OK. FASTER

### DICTIONARY = A collection of {key:value} pairs
### Ordered and changeable. No duplicates
#capitals = {"USA": "Washington D.C.",
#            "India": "New Delhi",
#            "China": "Beijing",
#            "Japan": "Tokio"}
#print(capitals.get("USA"))

