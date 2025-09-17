# CodingInterview

This repo is disgned to be a cheat sheet of python to coding interviews

## Sorting
```python
elements = [5, 3, 6, 2, 1]

elements.sort() # default for numbers is ascending  and for strings is alphabetical 

print(elements) # [1, 2, 3, 5, 6]
```
### sort parameters 
```python
sort(key, reverse)

key # custom sorting, it needs to be a function

words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]

words.sort(key=lambda word: len(word))

print(words) # ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']

reverse = True # reverts the default( numbers to descending )
```
### .sorted()
```python
elements = [5, 3, 6, 2, 1]

newList = sorted(elements) # create a sorted version of the elements and put it on newList

```
## Pythonic Code(python things)

### unpacking 

``` python
point1 = [0, 0]
point2 = [2, 4]

x1, y1 = point1 # x1 = 0, y1 = 0
x2, y2 = point2 # x2 = 2, y2 = 4

slope = (y2 - y1) / (x2 - x1)

print(slope) # Output: 2.0 
```

### loop unpacking
#### the for iterate through points considering the tuples as objects and executing one time by tuple

```python
points = [[0, 0], [2, 4], [3, 6], [5, 10]]

for x, y in points:
    print(f"x: {x}, y: {y}")

```

### enumerate
#### used to iterate in list and have both the value and index at the same time

```python
nums = [2, 7, 9, 2]

for index, value in enumerate(nums):
    print(index, value)
```

### zip
#### Allows to dynamically associate 2 lists in a single one with values correlated to the indexes ** lists need to be of the same length

```python
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [90, 85, 88, 92]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

## Lists in python

### Basics
```python
lista = [1,2,3]

lista.append(value) #ads the value to the end of the list
lista.pop() #remove the last item of the list
lista.insert(index, value) #adds the value on the specific index 
lista.index(value) #returns the index of the first occurance of the value on the list 
lista.remove(value) #remove the first occurance of the value on the list
lista.extend(list) #adds the list on the end of the other lista
```

### Concatenate
#### Instead of using extend we can use +

```python
list1 = [1,2,3]
list2 = [4,5,6]

list1 + list2 = [1,2,3,4,5,6]
list1.extend(list2) = [1,2,3,4,5,6]
```

### Initialization
#### If we need to create lists of specific sizes 

```python
my_list = [0] * 5 #would create a list of [0,0,0,0,0]
my_list = [1] * 3 #would create a list of [1,1,1]
```
### Copy
#### To clone a list we use the .copy() command

```python
list1 = [1,2,3]
clone = list1.copy()
```

### List Comprehension 
#### in Python we can create lists in concise way 

``` python
lis1 = [i for i in range(5)] # this creates the list [0,1,2,3,4]

result = [i for i in list1 if i % 2 ==0] #this would take the list1 and add to the result just the even numbers, so result would be [0,2,4]
```

## Stacks and Queues
### Stack
#### Python doesn`t have built in stack data structures but lists can be used just about the same

```python
stack = []
stack.append(value) #adds the value to the top of the stack
stack.pop() #removes the top element of the stack, and returns its value
stack[-1] #will always have the top element
```

### Queue 
#### queue are implemented in python using the deque structure which is a double ended queue

``` python
from collection import deque

queue = deque([3,4,5])

queue.append(1) # [3,4,5,1]
queue.append(2) # [3,4,5,1,2]

queue.popleft() # returns 1 and the queue now is [4,5,1,2]
leftmost = queue[0] # 4
rightmost = queue[-1] # 2

len(queue) #can be use as a isEmpty function 


