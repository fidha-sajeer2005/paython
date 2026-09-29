file = open("file.txt","r")
content= file.read()
print(content)
file.close()

file = open("file.txt","r")
print(file.read())
file.close()
