#creating a set
#using curly braces
my_set={1,2,3,4}
print(my_set)
#using set()function
another_set=set([5,6,7])
print(another_set)
#Empty set:
empty_set=set()
print(type(empty_set))
#Accesing set Items
my_set={10,20,30,40}
for item in my_set:
  print(item)
my_set={1,2,3}
print(2 in my_set)
print(5 in my_set)
#Adding Items to a Set
#Adding a Single Item:
my_set={1,2,3}
my_set.add(4)
print(my_set)
#Adding Multipple Items:
my_set={1,2,3}
my_set.update([4,5,6])
print(my_set)
#Removing Items from a Set
#remove()
my_set={1,2,3,4}
my_set.remove(2)
print(my_set)
#discard()
my_set={1,2,3,4}
my_set.discard(5)
print(my_set)
#pop()
my_set={1,2,3,4}
removed_item=my_set.pop()
print(removed_item)
#clear()
my_set={1,2,3}
my_set.clear()
print(my_set)
#Joining Sets
#union():
set1={1,2,3}
set2={3,4,5}
result=set1.union(set2)
print(result)
#update():
set1={1,2,3}
set2={4,5,6}
set1.update(set2)
print(set1)
#Set Intersections(&):
set1={1,2,3}
set={2,3,4}
result=set1 & set2
print(result)


