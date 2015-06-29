import os
import path import *
'''
cls_path = os.path.join("..", "src
for cls in os.listdir(cls_path):
	if os.path.isdir(os.path.join(cls_path, cls)):
		cls_src_path = os.path.join(cls_path, cls)
		# for information file 
		info_path = os.path.join(cls_src_path, "info.txt")
		# for 
		src_path = os.path.join(cls_src_path, cls+".py")
		print src_path
	'''	