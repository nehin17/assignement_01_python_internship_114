#Write a python program that counts the occurrences of a specific element in a list.
a=int(input("enter the element you want to count:"))
list1=[1,2,1,5,1,5,2,4,6,1,8,2,4,5,1,2,4,52,4,5,12]

#condition if teh speciifed element exists in the list
if a in list1:
    #using count() function
    print("element {} exists {} times".format(a,list1.count(a)))

#otherwise case
else:
    print("the specified elemnet does not exist in the list ")
