# if else elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# control the flow of your program based on conditions. 
# while loops execute long statement for true 
# for loops
i = 1
while i < 6:
  print(i)
  i += 1
  # Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# wap to write a table using loops
num=20
print(f"-------multiplication table")
for i in range(1,11):
    print(f"{num}*{i}={num*i}")

# calculate the sum of the five natural numbers
sum=0
for i in range(1,6):#loops 1 to 5
  sum +=i #sum=sum+i
print("sum:",sum)

#for i in range(start,end):
#starts is where the loop starts
#end is where the loop ends

# print nummbers in reverse (5to1)
# for i in range (5,0,-1):
  #start at 5 stop before 0 ,decrement by 1  print(i)  
# print squares of numbers from 1 to 5 
sum=0
for i in range(1,6):#loops 1 to 5
  sum+=i
  print(i*i)
# If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
# In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".


# Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

# You can also have an else without the elif:

# Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

# Example
# One line if statement:

# if a > b: print("a is greater than b")
# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# Example
# One line if else statement:

# a = 2
# b = 330
# print("A") if a > b else print("B")
# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:

# Example
# One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# And

# Example
# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# Example
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Example
# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
# Nested If
# You can have if statements inside if statements, this is called nested if statements.

# Example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")




