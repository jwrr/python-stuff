
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
