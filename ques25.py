#Write a program that copies the contents of one text file to another.
with open('file1.txt','r') as firstfile, open('file3.txt','w') as secondfile: 
	#opening both the files with aliases 
	
	for line in firstfile: 
			#writing in secondfile
			secondfile.write(line)
