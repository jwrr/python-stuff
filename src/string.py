#!/usr/bin/python3
import sys

str = "This is a string"
print(str)

str = "That's all folks has an embedded single quote"
print(str)

str = 'Foghorn said "If you can\'t take a joke, I suggest you avoid mirrors"'
print(str)

str = "Hello" + "World"
print(str)

str1 = "She came from Planet Claire."
str2 = "I knew she came from there."
str = str1 + "\n" + str2
print(str)
str = """Use triple quotes
for multi
line
strings.
or\nyou\ncan\nuse\nescape-n"""
print(str)

str = r"the\nquick\tbrpwm\\fox"
print(str)

str = """backshlash in triple quote prevents\
newline.
"""
print(str)

name = input("Who are you? I really want to know: ")
if name=="":
  name = "There"
print("Hello "+name)


