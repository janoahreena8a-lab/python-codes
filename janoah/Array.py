# Arrays
# ARRAYS ARE MORE MEMORY EFFICENT WHEN STORING LARGE AMOUNT OF NUMERIC DATA AND 
# THESE ARE FAST NUMERICAL OPERATIONS
# examples storing lage data sets of numbers matrices for calculation



# LIST COLLECTION OF MULTIPLE DATA TYPE MORE MEMORY AND THEY ARE EASY
# ARRAY COLLECTION OF SAME DATA TYPE LESS MEMORY AND DIFFICULT


# # # INSERT
import array 
numbers=array.array('i',[1,2,3,4,5])
numbers.insert(1,10)
print(numbers)
# Basic operations on arrya
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))



# removing element
import array 
numbers=array.array('i',[1,2,3,4,5,7,8,9,10])
numbers.remove(10)
print(numbers)

# Basic operations on arrya
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))

# import array 
# numbers=array.array('i',[1,2,3,4,5])
# print(numbers)

import array 
numbers=array.array('i',[1,2,3,4,5,])
print(0)
print(4)


import array 
array=('i',[1,2,3,4,5,6])
print(numbers[2:5])

import array 
numbers=array.array('i',[1,2,3,4,5,7,8,9,10])
print(numbers[::-1])

import array 
numbers=array.array('i',[1,2,3,4,5,7,8,9,10])
print(numbers[::2])


numbers=[5,10,15,20,25,30]
sliced=numbers[0:]
total=sum(sliced)
print("sliced number:",sliced)
print("sum:",total)


import array 
numbers=array.array('i',[1,2,3,4,5])
reversed_array=numbers[::-1]
print("reversed numbers:",reversed)

