# Creating a Dictionary
# Using curly braces
my_dict={"name":"john","age":30,"City":"New York"}
# Using the dict()constructor
another_dict=dict(name="alice",age=25,City="Los Angeles")
print(my_dict)
print(another_dict)
# Empty Dictionary
empty_dict={}
print(empty_dict) 
#2 Accessing Dictionary Items
# Accessing with Brackets:
my_dict={"name":"john","age":30}
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.get("salary"))
#3 Changing Dictionary Items
my_dict={"name":"john","age":30}
my_dict["age"]=31
print(my_dict)
my_dict["City"]="New York"
print(my_dict)
# Adding Items to a Dictionary
my_dict={"name":"john","age":30}
my_dict["City"]="New York"
print(my_dict)
# Removing Items From a Dictionary
#pop(key):
my_dict={"name":"john","age":30}
last_item=my_dict.popitem()
print(last_item)
# del statment:
my_dict={"name":"john","age":30}
del my_dict["age"]
print(my_dict)
#clear():
my_dict.clear()
print(my_dict)
# Copying a Dictionary
# Using copy()
original={"name":"john","age":30}
copy_dict=original.copy()
print(copy_dict)
# Using dict() constructer:
original={"name":"john","age":30}
copy_dict=dict(original)
print(copy_dict)
# Nested Dictionaries
nested_dict={
    "person1":{"name":"john","age":30},
    "person2":{"name":"Alice","age":25}
}
print(nested_dict["person1"]["name"])
# Dictionary Methods
# Key()
my_dict={"name":"john","age":30}
print(my_dict.keys())
# valuse

        