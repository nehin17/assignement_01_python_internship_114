#Write a program that reads data from a CSV file and prints it to the console.
import csv
#importing csv moduleto work with csv files

file = 'file2.csv'

#opening a file
with open(file, 'r'):

    #reading a file
    reader = csv.reader(file)

    #using for loop to iterate over the lines in csv file and print them
    for row in reader:
        print(row)