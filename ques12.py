#Write a python program that calculates the sum of the digits of a given number.

number = int(input("Enter a number: "))

#presetting a variable to 0
sum = 0

#using while loop to run the operations until the gievn number becomes 0
while number > 0:

    sum += number % 10
    # % gives the remainder.
    #in this case when we divide the number by 10 we get the number at ones place, hence giving us a digit.

    number //= 10  
    #Floor division is a division operation that returns the largest integer that is
    #  less than or equal to the result of the division.


print("The sum of digits of the given number is:", sum)

