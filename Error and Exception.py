# a=12
# b=0
# print(a/b)

# x=10
# y="john"
# print(x+y)

# age=int("hello")
# print(age)

# x=[1,2,4,5,]
# print(x[5])

# student={"name":"fidha"}
# print(student["fidha"])

# file=open("abc.txt")


# try:
#     a=12
#     b=0
# except Exception as e: 
#     print(e)

# try:
#     x=10
#     y="jhon"
# except Exception as e:
#     print(e)

# try:
#     age=int("hello")
#     print(age)
# except ValueError:
#     print("please enter a valid number")

# try:
#     x=[1,2,4,5]
#     print(x[5])
# except IndexError:
#     print("index is out of range")


try:
    num=int(input("enter a number:"))
    result=10/num
except ZeroDivisionError:
    print("divition by zero is not allowed!")
else:
    print(f"the result is {result}")
finally:
    print("this will always be printed.")

