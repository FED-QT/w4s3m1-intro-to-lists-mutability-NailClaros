# exercise.py
# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))

a += 1
print("After a += 1:", a, b, id(a), id(b))

x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))

# === at 1st a and b point to the same object, but after a += 1, a points to a new object.
# === at 1st x and y point to the same object, and after x.append(4), both x and y still point to the same object, but the object itself has changed.
# === This demonstrates the difference between mutable (like lists) and immutable (like integers) types

# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: build upper_names
upper_names = []
for n in names:
    temp = ""
    for x in range(len(n)):
        if x == 0:
            temp += n[x].upper()
        else:
            temp += n[x]
    upper_names.append(temp)

# Task B: enumerate over upper_names
for idx, name in enumerate(upper_names, start=1):
    print(f"{idx}: {name}")

# Task C: demo two list methods
# 1. insert
upper_names.insert(2, "Zoe")
print("\n\nInserted Zoe at index 2:")
print("After insert:", upper_names)

# 2. remove
upper_names.remove("Bob")
print("\nRemoved Bob:")
print("After remove:", upper_names)

# 3. sort
upper_names.sort()
print("\nSorted upper_names:")
print("After sort:", upper_names)
