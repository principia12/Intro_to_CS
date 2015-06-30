import os
from os.path import join 
from path import *


# auxillary function
def compare(sol_file, ans_file):
	op = ans_file.split("\\")[-2]
	if ans_file.split("\\")[-1] in os.listdir(join(sol_file, "..")):
		sol = open(sol_file)
		ans = open(ans_file)
		
		lines = ans.readlines()
		case_num = 0
		error = 0.0
		error_cases = []
		for ind, line in enumerate(sol.readlines()):
			if line == lines[ind] and line.startswith("test"):
				case_num = max(case_num, int(line[-2]))
			elif line != lines[ind]:
				error += 1
				error_cases.append(ind)
		
		res = [(case_num - error)/case_num, error_cases]
	else:
		res = [0, ["all"]]
	
	return res

''' 
For comparing the produced result and solution.
Write score summary and error cases for each contributor.
'''

cont_name = [] # list for name of contributors

for cont in os.listdir(score):
	cont_name.append(cont)

# score_dic = {cont_name : {method_name : [right_rate, [error_nums]}}
score_dic = {}
	
for cls in os.listdir(test):
	if os.path.isdir(join(test, cls)):
		for op in os.listdir(join(test, cls)):
			if os.path.isdir(join(join(test, cls), op)):
				# path for solution and ans directory
				cls_dir = join(join(test, cls), op)
				sol = join(cls_dir, "solution.txt")
				res = {}
				for cont in cont_name:
					ans = join(cls_dir, "%s.txt"%cont)
					'''
					res = {}
					res.update({op : compare(sol, ans)})
					score.update({cont:res})
					'''
					res.update({cont: compare(sol, ans)})
				score_dic.update({op: res})
		
# write score to file

for cont in score_dic.itervalues().next().keys():
	score_path = join(score, cont)
	print "Writing scores for %s"%cont
	for op in score_dic.keys():
		score_file = open(join(score_path, "%s_score.txt"%op), "w+")
		score_file.write(op + "\n")
		score_file.write("score : %f\n"%score_dic[op][cont][0])
		for elem in score_dic[op][cont][1]:
			score_file.write("error case : case %s"%elem)
		if score_dic[op][cont][1] == []:	
			score_file.write("No errorneous case")
	
		score_file.close()
	
	
	
	