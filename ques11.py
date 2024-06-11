#Write a python program that generates the first n numbers in the Fibonacci sequence.
#Fn = Fn-1 + Fn-2

n = int(input("enter the number of terms you want in your fibionacci sequence:"))
num1 = 0
num2 = 1
next_number = num2 
count = 1

print("fibbionaci sequence till {} terms is".format(n))

while count <= n:
	#the loop works n times generating n numbers
	
	print(next_number, end=" ")
	
    #increasing count 
	count += 1
	num1, num2 = num2, next_number
	
    #setting the number to be printed as the sum of the two digits before it
	next_number = num1 + num2

