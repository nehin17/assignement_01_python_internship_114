#Write a python program that calculates the factorial of a given number.

#the factorial of a number is calculated as n!= n* n-1* n-2*...*1

a=int(input("enter the number whose factorial you want to calculate:"))

if a==0 or a==1:
    #factorial of 0 and 1 is 1
    print("the factorial of",a ,"is: 1")

else:
   #pre setting a variable 
   result=1

   for i in range(2,a+1):
     #since we already did factorial for 1 we start with 2 in our range

     result *= i
     # 1*2*3...*a

   print("The factorial of",a, "is", result) 


