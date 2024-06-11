#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
a=int(input("do you want to convert\n 1.farenheit to celsius \n 2.celsius to farenheit \n:"))
#giving the user choice 
b=int(input("enter the temperature:"))

#choice 01
if a==1:
    c=(b-32)*(5/9)
    print("temperature in celsius is:",c,"deg C")

#choice 02
elif a==2:
    f=((9/5)*b)+32
    print("temperature in farenheit is:",f,"deg F")

#if wrong input is entered 
else:
    print("invalid input")