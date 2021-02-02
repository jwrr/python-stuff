#!/usr/bin/python3

print("hello")



# ===========================================================================
# Printing

print('Hello')        # single quotes and double quotes are the same')
print()               # print blank line
print(35+7)           # print expression
print(3.5 * 12)       # print float
print(7, 13, "cat", "dog", 42) # print multiple items

# print triple quote
print("""The triple-quote is used
for multiline strings
such as this one""")


# ===========================================================================
# Strings


strx = "DO NOT CREATE A VARIABLE NAMED 'str'. it will override Python's str method"
print(strx)

strx = "This is an 'embedded single quote'"
print(strx)

strx = 'this is an "embedded double quote"'
print(strx)

# String concatenation
strx = "Hello" + "World"
print(strx)

str1 = "First words"
str2 = "Lasgt words"
strx = str1 + "\n" + str2
print(strx)

# Triple quotes for multiline strings
strx = """Use triple quotes
for multiline
strings.
or\nyou\ncan\nuse\nescape-n"""
print(strx)

strx = """backshlash in triple quote prevents\
newline.
"""
print(strx)


# Raw String literals.
strx = r"the\nquick\tbrown\\fox"
print(strx)

# Repeat string
print('=' * 80)

# Prompt for input
# name = input("Who are you?")
# if name=="":
#   name = "Anon"
# print("Hello "+name)


# Reverse/Flip string
forwards = "Reverse this string!"
backwards = forwards[::-1]
print(forwards)
print(backwards)
print()


# Several ways to convert values to strings. f-strings is the newest (Python 3.6)
a = 1
b = 2
c = 3
print("a= "+str(a)+" b= "+str(b)+" c= "+str(c)+" concatinate with '+'")
print("a= %s b= %s c= %s c printf style (not recommended for python3)" % (a,b,c))
print("a= {0} b= {1} c= {2} use str.format".format(a,b,c) )
print(f"a= {a} b= {b} c= {c} use f-strings")

needle = "a"
haystack = "haystack"
boolean = needle in haystack
print( "'{}' in '{}' {}".format(needle, haystack, boolean) )


val = 42
if 41 < val < 43:
    print (f"val = {val} using 41 < val < 43")
else:
    print ("val out of range")


val = 0

if not val:
    print("'not val' is True when val==0 is")
else:
    print("val==0 is True??? Wrong")

empty_string = ""
if empty_string:
    print("Empty String is true???? Wrong")
else:
    print("Empty String is false??? Correct")



haystack = "Long String"
letter = "i"

if letter in haystack:
    print("{} is in {}".format(letter,haystack))
else:
    print("{} is not in {}.format(letter,haystack)")

letter = "s"
if letter in haystack.casefold():
    print("{} is in {} - use casefold to convert to lower".format(letter,haystack))
else:
    print("{} is not in {}.format(letter,haystack)")

for letter in haystack:
    print("{} is in {} - for letter in haystack".format(letter,haystack))



# Convert input to int
import random
highest = 10000
answer = random.randint(1, highest)
while True:
    guess = int(input("Guess between 1 and {}, inclusive. Enter 0 to quit: ".format(highest)))
    if guess == 0:
        print("Quitter.  The answer is {}".format(answer))
        break
    if guess < answer:
        print("Guess higher")
    elif guess > answer:
        print("Guess lower")
    else:
        print("Correct!")
        break


# Assign multiple variables to the same value
a = b = c = "abc"
print("{} {} {}".format(a,b,c))


# Create a simple menu

items = ["Quit", "Home", "School", "Work", "Camp", "Beach"]

selection = 0
while True:
    for item in items:
        print("{}: {}".format(items.index(item), item))
    selection = int(input("Where to? "))
    if 0 <= selection < len(items):
        break
    else:
        print("\nInvalid Selection. Please select again")
if selection == 0:
    print("Staying put")
else:
    print("Go to {} ".format(items[selection]))



# ===== d-bingame.py =====

#!/usr/bin/python

high = 10000
low = 1
max_guesses = 15

answer = int(input("Enter value between 1 and {}, inclusive: ".format(high) ))
for i in range(1,max_guesses):
    half = (high - low) // 2
    guess = low + half
    print("{}: {}".format(i,guess) )
    if guess > answer:
        high = guess - 1
    elif guess < answer:
        low = guess + 1
    else:
        print("correct")
        break
else:
    print("Failed to guess answer")

# ===== e-types.py =====
#!/usr/bin/python3

import sys

i = 42;
print ('i =', i, "of type", type(i))

i = "cat"
print ('i =', i, "of type", type(i))

i = 42
print( type(type(i)) )

# numeric   int float complex
# iterator
# sequence  str
# mapping
# file
# class
# exception



#

# ===== f-lists.py =====

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for plant in data:
    if "Shrub" in plant:
        shrubs.append(plant)
    else:
        flowers.append(plant)

print(shrubs)
print("join: " + ", ".join(shrubs))
print()
print(flowers)
print("join: " + ", ".join(flowers))
print()

ilist = range(10)
print(ilist)

numstr = "1 2 3 4 5 6 7"
slist = numstr.split(" ")
print(slist)


print("for-loop to convert list of string to int")
iilist = []
for s in slist:
    iilist.append( int(s) )
print(iilist)


print("list comprehension to convert list of string to int")
ilist = [int(s) for s in slist ]
print(ilist)

print("map to convert list of string to int")
ilist = list(map(int,slist))
print(ilist)


