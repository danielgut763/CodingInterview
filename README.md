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
