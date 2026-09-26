#1. Create a list [1,2,3] and add 4 to the end using a list method.
numbers=[1,2,]
numbers.append(4)
print(numbers)
#2. Given [10,20,30] , remove 20 using a list method.
numbers=[10,20,30,]
numbers.remove(20)
print(numbers)
#3. From [5,3,9,1,] sort the list in ascending order using a list method.
numbers=[5,3,9,1]
numbers.sort()
print(numbers)
#4. From [1,2,3,4,5] , extract 2,3,4 using slicing only.
numbers=[1,2,3,4,5]
print(numbers[1:4])
#5. Reverse the list [1,2,3,4] using slicing (no loops).
numbers=[1,2,3,4]
print(numbers[::-1])
#6. Combine [1,2] and [3,4] into one list using list operations.
a=[1,2]
b=[3,4]
print(a+b)
#7. Convert [7,8] into [7,8,7,8] using list operations.
numbers=[7,8]
print(numbers*2)
#8. Check if 3 exists in [1,2,3,4] using a list operator.
numbers=[1,2,3,4]
print(3 in numbers)
#9. Count how many times 2 appears in [1,2,2,3,2] using a list method.
numbers=[1,2,2,3,2]
print(numbers.count(2))
#10. Remove the last element from ["a","b","c","d"] using a list method.
x=["a","b","c","d"]
x.pop()
print(x)
#11. Insert "x" at index 1 in ["a","b","c"] using a list method.
x=["a","b","c"]
x.insert(1,"x")
print(x)
#12. Replace the element at index 2 in [10,20,30,40] with 99 using indexing.
x=[10,20,30,40]
x[2]=99
print(x)
#13. Convert range(5) into a list using list functions.
x=list(range(5))
print(x)
#14. Using slicing, extract every 2nd element from [1,2,3,4,5,6] → expected [2,4,6]
x=[1,2,3,4,5,6]
print(x[1::2])
#15. Remove all elements from [1,2,3] using one list method.
x=[1,2,3]
x.clear()
print(x)
#16. Copy a list [4,5,6] using only list tools (no modules).
a=[4,5,6]
b=a.copy()
print(b)
#17. Convert [1,2,3] into a nested list [1,2,3] using list operations.
a=[1,2,3]
a=[a]
print(a)
#18.Extend [1,2] with [3,4,5] using a list method.
a=[1,2]
a.extend([3,4,5])
print(a)
#19. Using list repetition, create a list ["hello","hello","hello"] .
a=["hello"]*3
print(a)
#20. Remove the element at index 2 from [10,20,30,40] using a list method.
a=[10,20,30,40]
a.pop(2)
print(a)
 
