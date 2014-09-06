#coding=utf-8

# 编写一个能搜索当前目录文件夹及其子文件夹内所有包含指定字符串的文件，并将文件路径打印出来的函数

import os

def search(s):
	for root, dirs, files in os.walk(os.path.abspath('.')):
		for h in files:
			if s in h:
				yield os.path.join(root,h)

# 现在来逐个打开这些文件，获得行数。

filenamelist=list(search('.cpp')) + list(search('.h'))

lines = 0

for filename in filenamelist:
	if not(("release" in filename) or ("debug" in filename)): #去掉release 和 debug 文件夹中的文件（IDE生成）
		fil = open(filename)
		while True:
			line = fil.readline()
			if not line:break
			if line != "\n":
				lines += 1
		fil.close()

print lines



