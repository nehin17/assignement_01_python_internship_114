#Write a program in python that counts the frequency of each character in a string.
str1=str(input("enter a string:"))

#converting the string to a list where each character is an element 
a=list(str1)

#convertingthe list to set soo that there is no duplicate items
set1= set(a)

#iterating over a set using a for loop
for item in set1:
    b=item

    #using count() fucntion we count the frequency of each element of set1
    print("the frequency of {} in the given string is {}".format(b,a.count(b)))