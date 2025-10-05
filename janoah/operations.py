# # Python Operators
# # Operators are used to perform operations on variables and values.

# # In the example below, we use the + operator to add together two values:

# # ExampleGet your own Python Server
# # print(10 + 5)
# # Python divides the operators in the following groups:

# # Arithmetic operators
x = 5
y = 3

print(x + y)


# # Assignment operators
x = 5

x += 3

print(x)
# # Comparison operators
x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3

# # ==	Equal	x == y	
# # !=	Not equal	x != y	
# # >	Greater than	x > y	
# # <	Less than	x < y	
# # >=	Greater than or equal to	x >= y	
# # <=	Less than or equal to	x <= y
# # Logical operators
x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10

# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
# # Identity operators
print(x == y)

# s 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y	

# # Membership operators
x = ["apple", "banana"]

print("banana" in x)

# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y	

# # Bitwise operators

# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	
print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


