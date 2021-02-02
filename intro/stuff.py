#!/usr/bin/python3

import sys




big_list1 = []
for i in range(10000):
    big_list1.append(i)
    
print(f"big_list1  bytes = {sys.getsizeof(big_list1)}")  

big_list2 = list(range(10000))
print(f"big_list2  bytes = {sys.getsizeof(big_list2)}")  

big_range = range(10000)
print(f"big_range bytes = {sys.getsizeof(big_range)}")  


def my_range(n :int):
    i = 0
    while i < n:
        yield i
        i += 1

big_range3 = my_range(10000)        
print(f"big_range3 bytes = {sys.getsizeof(big_range3)}")  


    
    
cond = True
x = 42 if cond else 7
print(x)

billion = 1_000_000_000
print(f"Put underscores in large numbers to make them more readable billion = {billion:,}")


infile = open("test.txt", "r")
entire_file = infile.read()
infile.close()
words = entire_file.split()
num_words = len(words)
print(f"Classic read file using open/close. num_words = {num_words}")

print("Use 'with' context manager to avoid forgetting to close file")
with open("test.txt", "r") as infile:
    entire_file = infile.read()
words = entire_file.split()
num_words = len(words)
print(f"num_words = {num_words}")



print("for loop with enumerate gives index")
a_list = list(range(10,20,2))
for i, val in enumerate(a_list):
    print(f"a[{i}]={val}")



print("for loop with zip itererates over two (or more) lists.")
firsts = ["W", "J", "R", "T"]
lasts = ["A", "B", "C", "D"]
for first,last in zip(firsts,lasts):
    print(first, last)
    
print("unpack into variables")
a_container = ("cat", "dog")
a1, a2 = a_container
print (a1, a2)

print("unpack remaining values")

a_list = list(range(10))
a, b, *remaining = a_list
print(a, b, remaining)


print("os.walk gets filelist similar to unix find command")
import os

root = "."
for path, directories, files in os.walk(root, topdown=True):
    print(path)
    for file in files:
        print('    ' + file)
    


print("donesss")

