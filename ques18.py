#Write a python program that checks if two strings are anagrams of each other
a=list(str(input("enter the first string:")))
b=list(str(input("enter the second string:")))
# anagrams are those words which have the same set of letters just different arrangements

c=a.sort()
d=b.sort()
# sorting the two lists for efficient comparison  

if c==d:
    #if all the elements are same i.e. both string contains same letters 
    print("the given strings are anagram")
    
else:
    print("the given strings are NOT anagram")