# introduction to errors and expections
# error mistake in the program that stops it from running correctly
# expeption error that happens while the program is running (runtime)
# types of errors
# compile-time errors(syntax error)
# happens when code is written incorrectly.
# example
# print("hello"#missing closing parantesis
# python will not run the program until fixed      
# logical errors
# program runs without crashing but gives wrong output
# intended:average of 2 numbers
# a,b=10,20
# print((a+b)/2)
# print((a+b)/3)
# runtime errors
# program starts running but crashes in middle due to invalid operations
# types of exceptions in pyhton
# some common exceptions
# zerodivisionerror=divideszero
# valuerror=wrongtypeofvalue
# indexerror=index out of range
# keyerror=key not keyNotFoundError
# FileNotFoundError=file dosent exist
# typeerror=operation on wrong data type
# exception handling in python
# we use try except finally to handle errors safely
# how is exceptional handiling done in python?
# try is the block of code that is monitored for errors except
#  the block gets excecuted when an error occurs
# try:
# a block of code where we write statements that may raise exceptions    
# except: 
#  ablock of code that handlesthe exceptions occurs in the try block
# finnally
# a block of code that allows excecute whether an exception occurs
# syntax:
# try
# code that may cause error 
# except<exception Type>:
# examplexs
# try:
#     num=int("abc")
#     result=10/10
# except value error:
# print(" invalid number")
# except zero division error :
# finally:
# print("done")
# example3
try:
    f=open("data.txt")
except Exception as e:
    print("Error:,e")
finally:
    print("file handiling attempted")