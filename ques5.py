#Write a program that takes a string input from the user and writes it to a text file.

a=str(input("enter a string:"))

#opening a file in our desired mode
file=open("output_file.txt","w")

#writing to our file
file.write(a)

#closing the file
file.close()