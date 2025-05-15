#Integer INT
x = int(1)
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# FLOAT -> Floating point number
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Casting
x = 1 # int
y = 2.8 # float
z = 1j # complex

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


# Random Number
import random
print(random.randrange(1, 10))



# Specify a variable type

# Integer
x = int(1)       # x will be 1
y = int(2.8)     # y will be 2
z = int("3")     # z will be 3

# Float
x = float(1)      # x will be 1.0
y = float(2.8)    # y will be 2.8
z = float("3")    # z will be 3.0
w = float("4.2")  # w will be 4.2

# String
x = str("s1")     # x will be 's1'
y = str(2)        # y will be '2'
z = str(3.0)      # z will be '3.0'