#Write a python program that checks if a substring is present in a given string.
str1="this is a question of string functions"
a=(input("enter the substring you want to find:"))

#find()-> helps us to find a substring and returns the index of the first occurence
# if the substring is not present then it returns -1 
b=str1.find(str(a))

#in case substring is not present
if b==-1:
    print("the given substring is not present in the string")
    
else:
    print("the given substring is present in the string at",b,"position")