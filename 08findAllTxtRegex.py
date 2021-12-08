# 找出路径下所有 txt 中满足正则表达式的行，输出

import re
import os

path = input('请输入路径:')
a = os.listdir(path)  # 列出指定目录下所有的文件名和文件夹名，并赋给 a

text = ''  # 初始化text变量

for i in range(len(a)):  # 迭代 a 中所有元素，找出符合要求的元素
    # 判断是否为 txt 文件
    if os.path.isfile(os.path.join(path, a[i])):
        if os.path.splitext(os.path.join(path, a[i]))[1] == '.txt':
            # 读取 txt 文件中的内容，并加到 text 变量里
            with open(os.path.join(path, a[i]), 'r') as f:
                text += f.read()

rg = re.compile(r'\d+')  # 创建正则表达式
text2 = rg.findall(text)  # 找出匹配正则表达式的内容
print(text2)  # 输出结果