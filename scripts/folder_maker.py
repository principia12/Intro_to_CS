import os
from path import *


'''
For making folder for all contributors
For each contributor, folder in src (for their source file) and folder in score should be given. Folders should contain test result. 
'''
def createPath(path):
	if not os.path.exists(path): 
		os.makedirs(path)


contrib = open(os.path.join(src, "contributors.txt"))

for line in contrib.readlines():
	createPath(os.path.join(src, line.strip("\n")))
	createPath(os.path.join(score, line.strip("\n")))
	
'''
Read the classname.txt file in test folder, and make folder for each class for containing test cases and solution. 

'''
	
for info in os.listdir(test):
	if info.endswith("txt"):
		info_file = open(os.path.join(test, info))
		# folder for each class
		cls_path = os.path.join(test, info[:-4])
		createPath(cls_path)
		for line in info_file.readlines(): 
			#print line.strip("\n")
			createPath(os.path.join(cls_path, line.strip("\n")))
		createPath(os.path.join(cls_path, "test cases"))
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		