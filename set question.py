#1. Create a set with values {1, 2, 3, 4}.
x={1,2,3,4}
print(x)
#2. Add the value 5 to the set {1, 2, 3, 4} using a set method.
x={1,2,3,4}
x.add(5)
print(x)
#3. Remove the value 3 from the set {1, 2, 3, 4} using a set method.
x={1,2,3,4}
x.remove(3)
print(x)
#4. Check if 2 exists in the set {1, 2, 3, 4} .
x={1,2,3,4}
print(2 in x)
#5. Convert the list [1, 2, 2, 3, 4, 4] into a set to remove duplicates.
x=[1,2,2,3,4,4]
y=set(x)
print(y)
#6. Convert the tuple (10, 20, 30) into a set.
x=(10,20,30)
y=set(x)
print(y)
#7. Find the union of sets {1, 2, 3} and {3, 4, 5} .
x={1,2,3}
y={3,4,5}
print(x.union(y))
#8. Find the intersection of sets 1, 2, 3 and 3, 4, 5 .
