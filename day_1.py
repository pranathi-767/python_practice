#day 01
#07.07.2025

print("Hello World!")

# This is a comment
"""
This is also a comment
but in 2 lines
"""

#variables
x = 4
y = 'John'
print(x)
print(y)
print(type(x))
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a+', '+b+', '+c)

#datatypes
d = 1.63
e = 1j
f = 89
print(type(d))
print(type(e))
print(type(f))

#strings
for g in "banana":
    print(g)

h = "Python is \"awesome\""
print(len(h))
print("is"in h)
if "is" in h:
    print("Yes")
if "are" not in h:
    print("No")
print(h[2:5])
print(h[:4])
print(h[6:])
print(h[-4:-2])

i = "great"
print(i.upper())
print(i.lower())

j = " Hello@ World!"
print(j.strip())
print(j.replace("H", "K"))
print(j.split("@"))

name = "ammu"
age = 20
k = f"My name is Ammu, I am {age}"
print(k)
print(f"My name is {name}, I am {age}")

#done for the day
