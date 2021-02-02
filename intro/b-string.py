#!/usr/bin/python3
import sys

strx = "This is a string"
print(strx)

strx = "That's all folks has an embedded single quote"
print(strx)

strx = 'Foghorn said "If you can\'t take a joke, I suggest you avoid mirrors"'
print(strx)

strx = "Hello" + "World"
print(strx)

str1 = "She came from Planet Claire."
str2 = "I knew she came from there."
strx = str1 + "\n" + str2
print(strx)
strx = """Use triple quotes
for multi
line
strings.
or\nyou\ncan\nuse\nescape-n"""
print(strx)

strx = r"the\nquick\tbrpwm\\fox"
print(strx)

strx = """backshlash in triple quote prevents\
newline.
"""
print(strx)

print('=' * 80)

# name = input("Who are you?")
# if name=="":
#   name = "There"
# print("Hello "+name)


forwards = "Reverse this string!"
backwards = forwards[::-1]
print(forwards)
print(backwards)
print()

a = 1
b = 2
c = 3
print("a= "+str(a)+" b= "+str(b)+" c= "+str(c)+" concatinate with '+'")
print("a= %s b= %s c= %s c printf style (not recommended for python3)" % (a,b,c))
print("a= {0} b= {1} c= {2} use str.format".format(a,b,c) )
print(f"a= {a} b= {b} c= {c} use f-strings")

needle = "a"
haystack = "haystack"

boo = needle in haystack
print( "'{0}' in '{1}' {2}".format(needle, haystack, boo) )


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
        print("Correct! U R A WEENER!")
        break

print("=" * 80)
a = b = c = "abc"
print("{} {} {}".format(a,b,c))



