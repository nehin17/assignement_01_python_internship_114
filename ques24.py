#Write a program that acts as a simple calculator. 
# It should take two numbers and an operator (+, -, *, /) as input and print the result.
a=int(input("enter the first number:")) 
b=int(input("enter the second number:"))

#giving the user choice
dict1={1: "addition", 2:"subtraction", 3:"multiplication", 4:"division"}
print(dict1)

#asking for users choice
c=int(input("enter the choice of operation you want to perform:"))

#choice 1
if c==1:
    print("addition of the given numbers is:",a+b)

#choice 2
elif c==2:
    print("subtraction of the given numbers is:",a-b)

#choice 3
elif c==3:
    print("multiplication of the given numbers is:",a*b)

#choice 4
elif c==4:
    print("division of the given numbers is:",a/b)

#if wrong input is given
else:
    print("ERROR! wrong input")

