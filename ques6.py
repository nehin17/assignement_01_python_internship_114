#Write a program that reads the content of a text file and prints it to the console.

#opening a file using file directory
file=open("C:/Users/Anand/Desktop/programs/PYTHON INTERNSHIP/files/file1.txt", "r")

#iterating over the file using for loop
for row in file:

    #reading all the lines of file and printing it as a list using readlines() function
    a=file.readlines()

    print(a)