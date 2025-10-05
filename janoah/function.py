# # a function is a block of code that is usedto perform a specific task 
# its a block of reusable code
# # keyword = def to define a function 

# # why use functions?
# # avoid repetation code make code organized easy to debug and maintain
# higher order functions
# these are functions that either:
# take another function as an argument 

# map()
# applies a function
def square(x):
    return x*x
numbers=[1,2,3,4,5]
squared=list(map(square,numbers))
print(squared)

# filter()
# filter items in an iterable based on a function that returns true/false
def is_even(x):
    return x %2==0
numbers=[1,2,3,4,5,6]
even_numbers=list(filter(is_even,numbers))
print(even_numbers)

# reduce()
# reduce a list to a single value by applying a binary function repeatedly
# from functools import reduce
# def add(x,y):
#     return x+y
# numbers=[1,2,3,4,5]
# sum_numbers=reduce(add,numbers)


# # syntax:
# # def function_name
# # print("hello,world!")


# # example
# def greet():
#     print("Welcome to python functions!")
#     greet()


# # passing parameters and arguments
# # example
# def greet_user(name):
#     print('hello,',name)    

# # calling function with argument 
# greet_user("hero")

# # # output hello,hero

# # function arguments types
# # positional arguments
# # arguments are passed in order 
# # example:
# def add(a,b):
#     print("sum is:",a+b)
#     add(5,10)

# # keyword arguments
# # specify arguments by parameter name.
# # example:
# def introduce(name,age): 
#     print(f"my name is{name} and I am{age}years old.")   
#     introduce(age=29,name="hero")


# # default arguments
# # if no argument is passed defalt ValueError
# # example:
# def greet(name="Guest"):
#     print("Hello, ",name)
# greet()     
# greet("ram")


# # local variable declared inside a function accesible inside
# # global variable decleared outside all functions

# # example global vs local 
# x=100
# def fun():
#     # local variable
#     y=50
#     print("inside function,x=",x)
#     print("inside function,x=",x)

#     print("outside function ,x=",x)
#     print(y)


# a=int(input("enter first number"))
# b=int(input("enter second number"))
# def mul_numbers(a,b): 
#     return a*b
# print("Multiplication:",mul_numbers(4,3) )  

# num=int(input("enter a number"))
# def even_odd_check(n):
#     if n%2==0:
#         print(n,"is even")
#     else:
#         print(n,"is odd")

# num=int(input("enter a number"))       
# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result*=i
#         return result
#     print(factorial(num))

# n1=int(input("enter a number"))    
# n2=int(input("enter a number"))
# n3=int(input("enter a number"))            

# def largest_of_three(a,b,c):  
#     if a>=b and a>=c:
#         return a
#     elif b>=a   and b>=c:
#         return b
#     else:
#         return c
# print(largest_of_three(n1,n2,n3))     



# str=input
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string(str))

# word=int(input("enter your name"))
# def count_vowels(word) :
#     vowels="aeiouAEIOU" 
#     count=0
#     for char in word:
#         if char in vowels:
#             count +=1
#             return count
#         print(count_vowels(word))  



