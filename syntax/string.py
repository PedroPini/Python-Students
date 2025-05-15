# Multiple lines assigning to a variable
# Option 1
a = "Hello this is " \
"a very long" \
" text"

# Option 2
a = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''



# String as Array ["H", "e", "l", "l", "o", ",", " ", "W", "o", "r", "l", "d"]
a = "Hello, World!"
print(len(a))
# Loop through using FOR
for printing in a:
    print(printing)
print(a[0])


# Check String
txt = "The best things in life are free!"

print("free" in txt)

# IF AND ELSE STATEMENTS
if "free" in txt:
    print("Yes, 'free' is present")

# Not IN
print("things" not in txt)

if "free" not in txt:
    print("No, 'free' is not present")
else:
    print("Yes, It's present")


# Slicing
b = "Hello, World!"
print(b[2:5])