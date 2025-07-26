# write a program in python to swap two numbers
#let's take input from user
num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2:"))
#print before swapping
print(f"Before Swapping num1={num1},num2={num2}")
temp=num1
num1=num2
num2=temp
#print after swapping
print(f"After Swapping: num1={num1},num2={num2}")