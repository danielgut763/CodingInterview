# CodingInterview

This repo is disgned to be a cheat sheet of python to coding interviews

## Sorting

elements = [5, 3, 6, 2, 1]

elements.sort() -> default for numbers is ascending  and for strings is alphabetical 

print(elements) # [1, 2, 3, 5, 6]

### sort parameters 

sort(key, reverse)

key -> custom sorting, it needs to be a function

words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]

words.sort(key=lambda word: len(word))

print(words) # ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']

reverse = True -> reverts the default( numbers to descending )

### .sorted()

elements = [5, 3, 6, 2, 1]
newList = sorted(elements) -> create a sorted version of the elements and put it on newList


## Pythonic Code(python things)
