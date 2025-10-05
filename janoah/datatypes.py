# concentration of two strings
first_name =input("enter first name:")
last_name =input("enter last name:")
print("Full name:", first_name+"" +last_name)
# string repetation
print("repeated name:",first_name*3)
# string length
print("length of string:",len(first_name))
# string conversion 
print("string to upper case:", first_name.upper())
print("string to lower case:", last_name.lower())
# swap case
print("swap case:", last_name.swapcase())
# all data types
# Numeric types int str float
# Sequence types str listt[]tuple()range:
# mapping type disct{}
# Set types set{}frozenset:
# Boolean type true or false
# Binary types bytes bytearray
# none types
# x = str("Hello World")	str	
# x = int(20)	int	
# x = float(20.5)	float	
# x = complex(1j)	complex	
# x = list(("apple", "banana", "cherry"))	list	
# x = tuple(("apple", "banana", "cherry"))	tuple	
# x = range(6)	range	
# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	bool	
# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# Boolean Values
# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

# ExampleGet your own Python Server
print(10 > 9)
print(10 == 9)
print(10 < 9)
# When you run a condition in an if statement, Python returns True or False:

# Example
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")