class Stack(): 
    def __init__(self, contents):
        self.contents = contents
        
    def pop(self):
        if self.contents:
            return self.contents[-1]
        else:   
            return None
    def push(self, elem):
        self.contents.append(elem)
        

# producing operation result to root/test/class_name/method_name

import os
from os.path import join 

test = "..\\..\\..\\test"
cases_lst = []


cont_name = os.path.abspath(os.path.join(".", os.pardir)).split("\\")[-1]


for dir in os.listdir(test):
	if os.path.isdir(join(test, dir)) and dir == "Stack":
		test_cases = open(join(join(test, dir), "test cases.txt"), "r")
		for line in test_cases.readlines():
			line = line.strip("\n")
			if not line.startswith("test"):
				cases_lst.append(Stack([int(elem) for elem in line.split()]))
	
		test_cases.close()
		
		for op in os.listdir(join(test, dir)):
			if os.path.isdir(join(join(test, dir), op)):
				result = open(join(join(join(test, dir), op), "%s.txt" %cont_name), "w+")
				ind = 0
				for case in cases_lst:
					ind += 1
					result.write("test case #%d\n"%ind)
					if op == "pop":
						result.write(str(case.pop())+ "\n")
					elif op == "push":
						res = case.push(1)
						for elem in case.contents:
							result.write(str(elem) + " ")
						result.write("\n")
					else:
						print "No such method"


						