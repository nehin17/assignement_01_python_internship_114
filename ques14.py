# reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

print("Enter multiple lines of input. Press Enter on an empty line to finish.")

#creating an empty list
lines = []


while True:
    #taking input
    line = input("Enter a line (or press Enter to finish): ")

    #adding the user input to the emty list we created 
    if line:
        lines.append(line)

    else:
        #exiting the loop when enter is pressed i.e. empty line is given as an input
        break

print("\nYou entered the following lines:")

#iterating over the list to print the whole list
for line in lines:
    print(line)
