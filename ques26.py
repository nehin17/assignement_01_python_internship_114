#Write a program in python that checks if a string starts with a given preffix or ends with a given suffix.

a=str(input("enter the preffix or suffix you want to check for:"))
str1="unfinished"
b=str1.find(a)

#when the substring is present
if a!= -1:
    #condition for preffix. it would not be present in the last indexes
    if b in range(0,len(a)-1):
        
        print("the substring is present in the string as preffix")

    #if its not a preffix then its a suffix
    else:
        print("the substring is present in the string as suffix")

#if the substring is not present 
else:
    print("the given preffix/suffix is NOT present in the string")