#Write a python program that takes a list of numbers and returns their sum.
list1 = []

#taking the length of the list
count = int(input("Enter the total count of elements in the list: "))

for i in range(count):
    
    # since i take values as count-1 we use i+1 in formatting
    value = int(input("Enter value {}: ".format(i+1)))

    # adding the input as the new element in the empty list
    list1.append(value)

print("the generated list is:\n",list1)

#using sum() function
print("sum of all the elements in the list is:", sum(list1))