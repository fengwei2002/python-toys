# 编写一个程序，在一个文件夹中，找到所有带指定前缀的文件，诸如 spam001.txt, spam002.txt 等，
# 并定位缺失的编号（例如存在 spam001.txt 和 spam003.txt，但不存 在 spam002.txt）。
# 让该程序对所有后面的文件改名，消除缺失的编号。

import re
import os
import shutil

path = input('input search path')
prefixName = input('input prefix (not include number)')

prefixRegex = re.compile(r'\%s\d\d\d.*' % (prefixName))
numberRegex = re.compile(r'\d\d\d')

fileList = []
for fileName in os.listdir(path):
    if os.path.isfile(os.path.join(path, fileName)):
        if prefixRegex.search(fileName):
            fileList.append(fileName)

print(fileList)

for i in range(len(fileList)):
    if i == 0:
        continue    
    a = numberRegex.search(fileList[i]).group()
    b = numberRegex.search(fileList[i - 1]).group()

    if (int(a) - int(b) > 1):
        fixNum = int(numberRegex.search(fileList[i - 1]).group()) + 1
        extendName = os.path.splitext(os.path.join(path, fileList[i]))[1]
        fixFileName = r'%s%03d%s' %(prefixName, fixNum, extendName)

        shutil.move(os.path.join(path, fileList[i]), os.path.join(path, fixFileName))
        fileList[i] = fixFileName

print(fileList)