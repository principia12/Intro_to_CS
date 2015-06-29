import os
from os.path import join 
from path import *


''' 
For comparing the produced result and solution.
Write score summary and error cases for each contributor.
'''

for cls in os.listdir(test):
	if os.path.isdir(join(test, cls)):
		for op in os.listdir(join(test, cls)):
			if os.path.isdir(join(join(test, cls), op)):
				sol = os.listdir(join(join(test, cls), op))[1]
				ans = os.listdir(join(join(test, cls), op))[0]
				
		

for cont in os.listdir(score):
	res = join(join(score, cont), "score.txt")
	
