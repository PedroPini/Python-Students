#console.log alternative
print("Hello World")


#Indentation -> Best practice: use 4 spaces per indentation level.
def greet(name):
    if name:
        print("Hello, " + name)
        print("Nice to meet you")
    else:
        print("Hello, stranger!")


greet("Eliza")

## Semicolons ;
print("Hello, World!")


# Here you have a comment

# Variables
this_is_number_five = 5
name = "John"
print(this_is_number_five, name)

# Casting
age = int(20)
namePedro = str("Pedro")
print(namePedro, type(namePedro))
print(age, type(age))

# Double or Single Variables
x = "John"
# is the same as
x = 'John'

# Case Sensitive -> a or A it will be different
Ball = 'adidas'
ball = 'nike'

##print(Ball, ball)


# Variable Naming
# only alpha-numeric characters and underscores(A-z, 0-9, and _ )
# Cannot be a python keyword https://www.w3schools.com/python/python_ref_keywords.asp

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Camel Case -> Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case -> Each word starts with a capital letter: 
MyVariableName = "John"  

# Snake Case -> Each word is separated by an underscore character: 
my_variable_name = "John" 

# Assiging Variables
fruit1, fruit2, fruit3 = "Orange", "Banana", "Cherry"
print(fruit1)
print(fruit2)
print(fruit3)

# One value to multiple variables
salad1 = salad2 = salad3 = "Lettuce"
print(salad1)
print(salad2)
print(salad3)

# Unpack a variable into python

fruits = ["apple", "banana", "cherry"]

apple, banana, cherry = fruits

print(apple)
print(banana)
print(cherry)

#How to Print -> equal to console.log in javascript
x1 = "Python is awesome" 
print(x1)  

# Printing 2 case
x = "Python" 
y = "is" 
z = "awesome" 
print(x, y, z) 

# Printing 3 case
x = "Python " 
y = "is " 
z = "awesome" 
print(x + y + z) 

# Print number
x = 5 
y = 10 
print(x + y)  

# Error when we try to Sum Number with String
x = 5 
y = "John" 
print(x + y) 

# Print Number and string
x = 5 
y = "John" 
print(x, y) 