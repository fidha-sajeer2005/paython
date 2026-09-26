# Paython Strings Overview
my_string="Hello, world!"
#1 String Slicing
# Basic Slicing
s="Hello, world!"
print(s[0:5])
# Negative Indices
s="Hello, world!"
print(s[-6:-1])
# Skipping Characters:
print(s[0:12:2])
# Reversing a String
print(s[::-1])
#2 Modifying Strings
# Replace method
s="Hello, world!"
new_s=s.replace("world","python")
print(new_s)
# Uppercase and Lowercase Conversion
print(s.upper())
print(s.lower())
#3 String Concatenation
# Using+Operator
s1="Hello" 
s2="World"
result=s1+"",""+s2+"!"
print(result)
# Using join() Method
Words=["python","is","awesome"]
sentence="".join(Words)
print(sentence)
# Format Strings
# Using % Operator
name="Alice"
age=25
formated_string="my name is Alice,and Iam age 25 years old"
print(formated_string)
# Usying Format()method
# Keyword Arguments:
# Using f-strings(python3.6+):
# Escape characters
# Common Escape Characters:
#. \n:Newline
#. \t:Tab
#. \':Single quot
#. \":Doble
#. \\:Backslash
# Inserting a newline
print("Hello\nWorld")
# Inserting a tab
print("Hello\tWorld")
# Using quotes within a string
print('He said,"python is amazing!"')
# String Methods
# len():
s="Hello, World!"
print(len(s))
# Strip():
s= "Hello, World!"
print(s.strip())
# Split():
s="Hello, World!"
print(s.split(","))
# Find():
s="Hello, World!"
print(s.find("World"))
# Count():
s="Hello,Hello,World!"
print(s.count("Hello"))
# Startswith()and endswith():
s="Hello, World!"
print(s.startswith("Hello"))
print(s.endswith("World!"))
# Upper() and Lower():
s="Hello, World!"
print(s.upper())
print(s.lower())
# replace():
s="Hello, World!"
print(s.replace("World"," Python"))