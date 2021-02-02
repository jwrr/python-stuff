#!/usr/bin/python3

import sys



# generator function yields (instead of returns) and starts immediately after
# yield when it's called again

def odds():
    i = 1;
    while True:
        yield i;
        i += 2;

for odd in odds():
    print(odd);
    if odd > 10:
        break









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



