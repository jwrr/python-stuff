#!/usr/bin/env python3

print("list comprehensions")

alist = range(10)
b = [a * 2 for a in alist]
print(b)

print("set comprehensions")
bset = {a ** 2 for a in alist}
print(bset)

text = "for score and seven years ago"
chars = [ch.upper() for ch in text]
print(chars)

words = [word.upper() for word in text.split(' ')]
print(words)

words_unchanged = text.split(' ')
print(words_unchanged)


print("join")
join_str = "-".join(["the", "quick", "brown", "fox", "jumped", "over"])
print(join_str)

print("What if all elements of list aren't strings?")

join_list2 = ["the", 5, "brown", "fox", "jumped", "over"]
join_str2 = "-".join([str(j) for j in join_list2])
print(join_str2)


lenlist = [len(word) for word in text.split()]
print(text)
print(lenlist)

tuplist = [(word, len(word)) for word in text.split()]
print(tuplist)


duptext = "for score and seven years ago for score and seven years ago for score and seven years ago for score and seven years ago "
tupset = {(word, len(word)) for word in duptext.split() }


inch = (2, 3, 4)
cm = tuple([i * 2.54 for i in inch])
print(cm)


print("Conditional Comprehensions ")

dlist = range(100)
mult3list = [m3 * 3 for m3 in dlist]
print(mult3list)

print("single filter")
div3list = [d3 for d3 in dlist if d3 % 3 == 0]
print(div3list)


print("double filter")
div3_notdiv6_list = [d6 for d6 in dlist if d6 % 3 == 0 if not d6 % 6 == 0 ]
print(div3_notdiv6_list)

print("single filter doing the same thing")
div3_notdiv6_listb = [d6 for d6 in dlist if d6 % 3 == 0 and not d6 % 6 == 0 ]
print(div3_notdiv6_listb)


print("Conditional Expression")

x = 42
expression = "Forty-two" if x == 42 else "Something else"
print(expression)

xx = [d6 if d6 < 30 else 777 for d6 in dlist if d6 % 3 == 0 and not d6 % 6 == 0 ]
print(xx)


print("Nested Comprehensions")

nouns = ["cat", "dog", "bird", "fish"]
adjs = ["fast", "slow", "big", "small"]

combolist = [" ".join((a,n)) for a in adjs for n in nouns]
print(combolist)


for combo in [" ".join((a,n)) for a in adjs for n in nouns]:
  print(combo)
  


for i in range(1,5):
  for j in range(1,5):
    print(i, i * j)


for ii, result in [(i, i*j) for i in range(1,5) for j in range(1,5)]:
  print(ii, result)
  

# Convert comprehension to generator by replacing '[]' with '()'
for ii, result in ((i, i*j) for i in range(1,5) for j in range(1,5)):
  print(ii, result)
  
  
print("Use timeit for benchmarking")

import timeit

setup = """\
import gc
gc.enable()
"""

loop_exec_str="""\
x = 0
for i in range(1000):
  for j in range(1000):
    x += i*j
"""
loop_time = timeit.timeit(loop_exec_str, setup=setup, globals=globals(), number=11)

comp_exec_str="""\
x = 0
for ii, result in [(i, i*j) for i in range(1000) for j in range(1000)]:
  x += i*j
"""
comp_time = timeit.timeit(comp_exec_str, setup=setup, globals=globals(), number=11)

gen_exec_str="""\
x = 0
for ii, result in ((i, i*j) for i in range(1000) for j in range(1000)):
  x += i*j
"""
gen_time = timeit.timeit(gen_exec_str, setup=setup, globals=globals(), number=11)
print(f"loop time = {loop_time}")
print(f"comp time = {comp_time}")
print(f"gen time  = {gen_time}")


# APPEND

loop_exec_str="""\
x = []
for i in range(1000):
  for j in range(1000):
    x.append(i*j)
"""
loop_time = timeit.timeit(loop_exec_str, setup=setup, globals=globals(), number=11)

comp_exec_str="""\
# x = []
# for ii, result in [(i, i*j) for i in range(1000) for j in range(1000)]:
#   x.append(i*j)
x = [i*j for i in range(1000) for j in range(1000)]
"""
comp_time = timeit.timeit(comp_exec_str, setup=setup, globals=globals(), number=11)

gen_exec_str="""\
x =  (i*j for i in range(1000) for j in range(1000))
"""
gen_time = timeit.timeit(gen_exec_str, setup=setup, globals=globals(), number=11)
print(f"loop append time  = {loop_time}")
print(f"comp append time  = {comp_time}")
print(f"gen append time   = {gen_time}")











