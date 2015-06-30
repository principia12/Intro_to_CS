# class definition

class Fortest():
	def __init__(self, n):
		self.n = n
		
	def __repr__(self):
		return "class for test, contains %d"%(self.n)
		
	def pprint(self):
		return self.n
		
	def addone(self):
		return self.n + 1
		

# producing operation result to root/test/class_name/method_name

import os
from os.path import join 

test = "..\\..\\..\\test"
cases_lst = []


cont_name = os.path.abspath(os.path.join(".", os.pardir)).split("\\")[-1]


for dir in os.listdir(test):
	if os.path.isdir(join(test, dir)):
		test_cases = open(join(join(test, dir), "test cases.txt"), "r")
		for line in test_cases.readlines():
			line = line.strip("\n")
			if not line.startswith("test"):
				cases_lst.append(Fortest(int(line)))
	
		test_cases.close()
		
		for op in os.listdir(join(test, dir)):
			if os.path.isdir(join(join(test, dir), op)):
				result = open(join(join(join(test, dir), op), "%s.txt" %cont_name), "w+")
				ind = 0
				for case in cases_lst:
					ind += 1
					result.write("test case #%d\n"%ind)
					if op == "pprint":
						result.write(str(Fortest.pprint(case))+ "\n")
					elif op == "addone":
						result.write(str(Fortest.addone(case)) + "\n")
					else:
						print "No such method"
			
						

	
	
	
	