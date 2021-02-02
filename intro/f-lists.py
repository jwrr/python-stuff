
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


