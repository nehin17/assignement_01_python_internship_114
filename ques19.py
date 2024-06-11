#Write a python program that removes all punctuation from a given string.
test_str = str(input("enter a string:"))

print("The original string is : " ,test_str)

#giving ll the punctuation signs
punc = '''!()-[]{};:'""\,<>./?@#$%^&*_~'''

#using for loop iterating over the string of punctuations and given string
for ele in test_str:
	if ele in punc:

		#replacing the common elemens found i.e. the punctuations with a blank space
		# replace() function is used
		test_str = test_str.replace(ele, "")

# printing result
print("The string after punctuation filter : " , test_str)
