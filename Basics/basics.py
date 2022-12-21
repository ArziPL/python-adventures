import random

if 5 > 2:
    print("Yes")

x = 5
y = "Hello world"

print(y)

# Comments
print(x)  # More comments


"""
Multiline
comment
"""

print(x)

x = 6
y = "Hello world!!!"
y = 3  # Variables can be changed

# Forcing the type
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x))


x = "string"
# the same as
y = 'string'

# Case sensitive
a = 4
A = "different"
print(a, A)


# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)


# Many values
x, y, z = 1, 2, 3
a = b = c = 4
print(x, y, z, a, b, c)


# Unpacking
my_array = [1, 2, 3]
x, y, z = my_array
print(x, y, z)

print("Hello " + "to " + "plus " + "sign")
print(5 + 4)  # Here as operator

x = 5


def myFunc():
    x = 6
    print(x)


print(x)  # They're not the same, global
myFunc()  # Local


def myFunc2():
    global x
    x = 7


myFunc2()  # Global keyword to change global variables
print(x)


# Data types

x1 = "string"  # string
x2 = 5  # int
x3 = 5.5  # float
x4 = 5j  # complex

# sequence
x5 = [1, 2, 3]  # list
x6 = (1, 2, 3)  # tuple
x7 = range(3)  # range

# mapping
x8 = {"name": "dict"}

x9 = {"set", "whatever", "it", "is"}
x10 = frozenset({"another", 1})

x11 = True

# ? binary ?
x12 = b"bytes here"
print(x12)  # string but type bytes
x13 = bytearray(10)
print(x13)  # this thing
x14 = memoryview(bytes(5))
print(x14)  # another this thing

# Just none
x15 = None

x = str("Hello")
x = int(20)
x = float(5.5)
x = complex(2j)
# Just iterable inside
x = list(("one", "two"))
x = tuple(("one", "two"))
x = range(6)
for i in x:
    print(i)
x = dict(name="John", surname="Doe")
x = set(("ite", "rable"))
x = frozenset(("frozen", "can't change"))
x = bool(1)

# ?
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
# ?

# e means to power of 10
x = 1.7e1
print(x)

# you can any number into any other but not complex to any other

# random, later
print(random.random())
print(random.randrange(1, 100))

x = int(2.8)  # int will cut decimals
print(x)

a = """
Multiline
string
here
"""

print(a)

# Python doesn't have char data type, 1 char is just 1 len string

a = "hello world"
print(a[4])

# You can iterate through string, it's iterable
for i in a:
    print(i, end="...")

# Len of string
print(len(a))

# Check if is in word
print("hello" in a)

# Check if IS NOT in word
print("not in word" not in a)

# Slicing string in range, from beginning, from end
print(a[0:5])
print(a[:5])
print(a[6:])

# Negative slicing (from end)
print(a[-1])

# String methods don't change original, returns new
# Upper, lower, remove whitespaces, replace, split words into list
a = "   hello, world   "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("h", "m"))
print(a.split(","))

a = "Hello"
b = "world"
print(a + " " + b)

a = "Formatting {} {}"
print(a.format("is", "cool"))

a = "Formatting {1} {0}"
print(a.format("cool", "is"))

print("Illegal \"characters\"")


# Most things return true, only 0, empty string, empty lists etc. returns false
print(True)
print(False)
print(bool(11))
print(bool("lol"))
print(bool(0))
print(bool(""))

# Operators
print(1 + 1 - 1 * 1 / 1)
print(10 % 3)
print(2**3)
print(5//2)

x = 2
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print(True and True)
print(True or True)
print(not False or False)

print(x is 2)
print(y is not 2)
print(x in range(1,10))
print(y not in range(20,100))

lists = ["this","list"]
print(lists)
print(len(lists))
print(type(lists))
new_list = list(("new","list"))
print(new_list)

test_list = ["hello","world","test","list"]
print(test_list[0]) # get specific index
print(test_list[1:3]) # get specific range of indexes
print(test_list[2:]) # get range from 2 to end
test_list[2] = "cool" # change third item of list
test_list[0:1] = ["world","hello"] # change range of indexes of list
test_list.append("new") # add at the end
test_list.insert(2,"middle") # add at specific index
test_list.extend(("tuple","test")) # add any iterable
test_list.remove("test") # removes specific value
test_list.pop() # removes last or specified index
test_list.pop(1)
del test_list[1] # also deletes item at specified index
for x in test_list: # iterate over items
    print(x)

for i in range(len(test_list)): # iterate over indexes
    print(i)

x = [x for x in test_list if "r" in x] # list comprehension
print(x)

# newlist = [expression for item in iterable if condition == True]

test_list.sort() # standard sort
test_list.sort(reverse=True) # reverse sort
test_list.reverse() # reverse order

test_list_2 = []
test_list_2 = test_list # THIS IS ONLY REFERENCE

# Correct ways to copy
a = test_list.copy()
b = list(test_list)

print("JOIN LISTS")
# Joining lists
join_lists = []
join_lists = join_lists + a
for i in a:
    join_lists.append(i)
join_lists.extend(a)
print(join_lists)