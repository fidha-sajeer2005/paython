# Creating a tuple
my_tuple=(1,2,3,'python',4.5)
print(my_tuple)
#Single Item Tuple:
single_tuple=(5,)
print(type(single_tuple))
#Accesing Tuple Items
my_tuple=('apple','banana','cherry')
print(my_tuple[1])
print(my_tuple[-1])
# Slicing Tuples:
my_tuple=(10,20,30,40,50)
print(my_tuple[1:4])
# Updating a tuple:
my_tuple=(1,2,3)
my_tuple=(4,5,6)
print(my_tuple)
#Convert tuple to list:
my_tuple=('apple','banana','cherry')
temp_list=list(my_tuple)
temp_list[1]='orange'
my_tuple=tuple=tuple(temp_list)
print(my_tuple)
#Unpaking Tuples
my_tuple=('apple','banana','cherry')
(fruit1,fruit2,fruit3)=my_tuple
print(fruit1)
print(fruit2)
print(fruit3)
# Using*(asterisk):
my_tuple=(1,2,3,4,5)
(first,*middle,last)=my_tuple
print(first)
print(middle)
print(last)
# Joining Tuples
tuple1=(1,2,3)
tuple2=(4,5,6)
joined_tuple=tuple1+tuple2
print(joined_tuple)
#  Tuple Methods
# Count()
my_tuple=(1,2,3,2,2,4)
print(my_tuple.count(2))
# Index()
my_tuple=('apple','banana','cherry')
print(my_tuple.index('banana'))
# Deleting a Tuple
my_tuple=('apple','banana','cherry')
del my_tuple
print(my_tuple)