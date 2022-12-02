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

x1 = "string" # string
x2 = 5 # int
x3 = 5.5 # float
x4 = 5j # complex

# sequence
x5 = [1,2,3] # list
x6 = (1,2,3) # tuple
x7 = range(3) # range

# mapping
x8 = {"name":"dict"}

x9 = {"set","whatever","it","is"}
x10 = frozenset({"another",1})

x11 = True

# ? binary ?
x12 = b"bytes here"
print(x12) # string but type bytes
x13 = bytearray(10)
print(x13) # this thing
x14 = memoryview(bytes(5))
print(x14) # another this thing

# Just none
x15 = None

x = str("Hello")
x = int(20)
x = float(5.5)
x = complex(2j)
# Just iterable inside
x = list(("one","two"))
x = tuple(("one","two"))
x = range(6)
for i in x:
    print(i)
x = dict(name="John", surname="Doe")
x = set(("ite","rable"))
x = frozenset(("frozen","can't change"))
x = bool(1)

# ?
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
# ?