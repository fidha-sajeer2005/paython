# Creating a List
my_list=[1,2,3,'python',4.5]
print(my_list)
# Accessing List Items
my_list=['apple','banana','cherry']
print(my_list[1])
print(my_list[-1])
# Range of Indexes:
my_list=[10,20,30,40,50]
print(my_list[1:4])
# Changing List Items
my_list=['apple','banana','cherry']
my_list[1]='orange'
print(my_list)
# Changing Multiple items:
my_list=[1,2,3,4,5]
my_list[1:3]=['a','b']
print(my_list)
# Adding Items to a list
# Append():
my_list=['apple','banana']
my_list.append('cherry')
print(my_list)
# insert():
my_list=['apple','banana']
my_list.insert(1,'cherry')
print(my_list)
# extend():
my_list=['apple','banana']
new_list=['cherry','orange']
my_list.extend(new_list)
print(my_list)
# Removing Items from a list
# Remove():
my_list=['apple','banana','cherry']
my_list.remove('banana')
print(my_list)
# pop():
my_list=['apple','banana','cherry']
popped_item=my_list.pop(1)
print(popped_item)
print(my_list)
# del():
my_list=['apple','banana','cherry']
del my_list[0]
print(my_list)
# clear():
my_list=['apple','banana','cherry']
my_list.clear()
print(my_list)
 #List Comprehensions 
# Syntax
squares = [x**2 for x in range(1, 6)]
print(squares) 
#Example with condition:
#  # Create a list of even numbers from 1 to 10
even_numbers = [x for x in range(11) if x % 2 == 0]
print(even_numbers)
# List Methods
# count():
my_list = [1, 2, 3, 2, 4]
print(my_list.count(2))
# index():
my_list = ['apple', 'banana', 'cherry']
print(my_list.index('banana'))
#reverse():
my_list=[1,2,3]
my_list.reverse()
print(my_list)
# sort():
my_list = [3, 1, 2]
my_list.sort()
print(my_list)
#copy():
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)
#Sorting a List
numbers = [3, 5, 1, 4, 2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
#sorted():
original = [3, 1, 4]
sorted_list = sorted(original)
print(sorted_list) 
# Copying a List 
original_list = ['apple', 'banana', 'cherry']
 # Using copy()method
copied_list = original_list.copy
 # Using slicing
copied_list = original_list[:] 
#Joining Lists 
# Using +:
list1 = ['apple', 'banana'] 
list2 = ['cherry','orange'] 
combined_list = list1 + list2
print(combined_list)
# Using extend():
list1 = ['apple', 'banana']
list2 = ['cherry', 'orange']
list1.extend(list2)
print(list1)
