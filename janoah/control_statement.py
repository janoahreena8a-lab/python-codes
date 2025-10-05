# [if condition]
# syntax
# code excute if the condition is true 
# example : checking the grade 
score = 90
if score>=90:
    print("excellent ; you have earned an A ")
"""
output : excellent ; you have earned an A 
"""
# [if else case ]
# syntax
# code to excute if condition is true 
# else 
# code to excute of condition is false
# example : checking if a num is even or odd
num = 5 
if num%2==0 :
    print(num, "is an even num ")
else :
    print(num ,"is an odd num ")


# [elif case]

marks=int(input("enter marks :"))
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=50:
    print("grade C")
else :
    print("fali")
# if else elif statement OR ELSE-IF LADDER
# wap to allocate gardes  for the given marks
score=78
if score>90:
    grade="A"
elif score>80: #else-if
    grade="B" 
elif score>70:
    grade="C"
elif score>60:
    grade= "D"   

else:
    grade="F"

print("THE-ELIF-ELSE STATEMENT")
print(f"A score of {score} gets  grade of {grade}.")   # f-string or formatted string 
print(f"A score of"+str(score)+"gets a grade of "+grade+ ".\n")
## 4.NESTED IF -ELSE STATEMENTS
# wap to find the numbers is graeter than 75 or not
num=78
if num>0:
    if num>25:
        if num>50:
            if num>75:
                print("The Nested If-Else Statements")
                print(f"{num} is greater than 75.\n")

else:
    print("The Nested If- Else Statements")    
    print(f"{num}is not greater than 75./n") 
        #keeping another or adding block of codes is called nested 
else:
    print("The Nested If else Statements") 
    print(f"{num} is not greater than 0.\n")  

