num=int(input("enter a number"))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")


#simple login system
correct_username="jano"
correct_password= "1234"
username=input("enter a username:")
password=input("enter a password:")
if username==correct_username and password==correct_password:
    print("acess granted")
else:
    print("acess denied")   

# break statement 
    for number in range(1,10):
        if number==5:
         print("breaking the loop at number 5")
        break 

# find the  first even number 
numbers=[3,7,9,12,15,18 ,19,21,] #numbers=[1,3,7,10,5,8]
for num in numbers:
    if num%2==0:
        print("first even numbers is:",num)
        break
    print(num)
# else:
#     print("no even number")   

# exit keyword
# wap to print exit to stop
while True:
    user_input=input("Enter 'exit' to stop:")
    if user_input =='exit':
        print("Exiting loop...")
        break
    print("You entered:",user_input)

