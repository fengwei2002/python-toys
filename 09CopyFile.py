# 遍历一个目录树，查找特的那个拓展名的文件（如，.jpg或.pdf）。
# 不论这些文件位置在哪里，将它们拷贝到一个新的文件夹中

import os
import shutil

fiName = input("请输入需要遍历的文件夹地址:")
baseName = input("请输入需要查找文件的拓展名（如：.pdf,.txt,.jpg）:")
toName = input("请输入需要移动到的地址：")

for folderName, _, filenames in os.walk(fiName):
    # os.walk 默认返回三个参数，因为第二个参数返回子文件夹用不上，因此设置了 - 参数，填充位置
    print('当前遍历文件夹：' + folderName)
    
    for filename in filenames:
        if filename.endswith(baseName):
            print("当前文件夹的“{0}”文件有：{1}".format(baseName, filename))
            filePath = folderName + '\\'+ filename
            shutil.copy(filePath, toName)
            print("拷贝文件“{0}”到“{1}”成功！".format(baseName, toName))