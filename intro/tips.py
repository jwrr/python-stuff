#!/usr/bin/python3


import sys
from collections import Counter

print("Use enumerate to get index and value")
l = [2,4,6,8]
for idx, val in enumerate(l):
    print(idx, val)
    
print("List Comprehensions")
x3 = [3*i for i in range(10)]
print(x3)

print("Use sorted reverse=True")
l1 = [1,3,5,7,9,2,4,6,8,0]

l2 = sorted(l1, reverse=True)
print(l1)
print(l2)

print("sort with lambda")
d1 = [{"name": "val", "age": 9},
      {"name": "wal", "age": 19}, 
      {"name": "jac", "age": 11}, 
      {"name": "rac", "age": 29}, 
      {"name": "rob", "age": 39}, 
      {"name": "jam", "age": 1}, 
     ]
     
d2 = sorted(d1, key=lambda x: x["age"])
print(d2)

print("Use set to remove duplicate elements")
l3 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,0,0,0]
s1 = set(l3)
l4 = sorted(s1)
print(l3)
print(l4)

print("Use generator to save memory with large lists")
l5 = [i for i in range(1000000)]
print(sum(l5))
print(sys.getsizeof(l5), "Bytes")
print("generators compute lazily, only when needed, one item at a time")
g5 = (i for i in range(1000000))
print(sum(g5))
print(sys.getsizeof(g5), "Bytes")

print("Set default values for dictionaries")

d3 = {"name": "rac", "age": 29}
print(d3)
count = d3.get("count") 
print(count)
if count == None:
    print("Count is None")
count2 = d3.get("count", 42)
print(count2)

print("Count objects with collections.Counter")
l6 = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,3,3,3,3,3,]
print(l6)
c6 = Counter(l6)
print(c6)
print("Get most_common, 2nd most common...")
mc = c6.most_common()
for cc in mc:
    print(cc)


print("Format strings with f-strings since 3.6")
name = "Rachel"
print(f"My name  is {name}")
for i in range(5):
    print(f"i={i}, i^2={i*i}")


print("Concatenate strings with .join")
l7 = ["hello", "good", "bye", "one", "two", "three"]
s7 = " ".join(l7)
print(s7)


print("Merge Dictionaries with ** notation new in 3.5")
d8  = {"name": "Rachel", "City": "Parts Unknown"}
d9  = {"name": "Rachel", "Age": 6}
d10 = { **d8, **d9}
print(d10)

l11 = ["red", "blue", "green"]
color = "red"
if color in l11:
    print(f"{color} is in list of colors")
