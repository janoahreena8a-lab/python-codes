# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:
# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# A list with strings, integers and boolean values:

# list1 = ["abc", 34, True, 40, "male"]
# type()
# From Python's perspective, lists are defined as objects with the data type 'list':

# <class 'list'>
# Example
# What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

# Example
# Using the list() constructor to make a List:

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# start
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# negative
# this example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

numbers=(1,2,3,2,1,2)
count_2=numbers.count(2)
print(count_2)

# index
fruits=('apple,bananna,mango,apple')
index_apple=fruits.index('apple')

# Continue
# used to skip the current iteration and continue withh the next one 
for number in range(1,6):
    if number==3:
        print("skipping the nuber 3:")
        continue
    print("numbers:" ,numbers) 

# skip negative numbers
list1=[1,-2,3,-4,5]
for num in list1:
     num<0
     continue
print(num)

# skip multiples of 3
for i in range(1,11):
    if i %3 ==0:
        continue
    print(i)
#  pass:
# acts as a placeholder when no action is needed(does nothing)   
# example
for number in range(1,4):
     if number==2: #do nothing
        pass    #do nothing
        print("number:",number)  

