#Create a string "hello" and convert it to uppercase using a string method.
s="Hello"
print(s.upper())
#Given "PYTHON" , convert it to lowercase using a string method
print(s.lower())
#From "hello world" , replace "world" with "python" using a string method.
s="Hello,world!"
new_s=s.replace("world","python")
print(new_s)
#Extract "ell" from "hello" using slicing only.
s="Hello"
print(s[1:4])
#Reverse the string "python" using slicing (no loops).
s="python"
print(s[::-1])
#Combine "hello" and "world" into one string using string operations.
s1="Hello"
s2="world"
result=s1+","+s2+"!"
print(result)
#Repeat the string "hi" to get "hihihi" using string operations.
result="hi"*3
print(result)
#Check if "cat" exists in "concatenate" using a string operator.
result="cat" in "concatenate"
print(result)
#Count how many times "a" appears in "banana" using a string method.
count="banana".count("a")
print(count)
#Remove leading and trailing spaces from " hello " using a string method.
result="hello".strip()
print(result)
#Find the index of "o" in "hello" using a string method.
index="Hello".index("o")
print(index)
#Split the string "a,b,c,d" into a list using a string method.
s="".join(["a","b","c"])
print(s)
#Extract every 2nd character from "abcdef" using slicing → expected "ace" .
s="abcdef"[::2]
print(s)
#Replace all "a" with "@" in "banana" using a string method.
s="banana".replace("a","")
print(s)
#Check if "hello123" is alphanumeric using a string method.
s="Hello123".isalnum()
print(s)
#Capitalize the first letter of "python" using a string method.
s="python".capitalize()
print(s)
#Convert "hello world" into "Hello World" using a string method.
s="Hello world".upper()
print(s)
#Remove all vowels from "python" using string operations (no loops if possible 😈).
s="python" 
result=s.translate(str.maketrans("","","aeiouAEIOU"))
print(result)
#Check if "madam" is a palindrome using slicing.
s="madam"
print(s == s[::-1])

