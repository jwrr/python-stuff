
#!/usr/bin/python

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


