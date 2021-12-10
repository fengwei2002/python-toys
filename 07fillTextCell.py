# 实现一个选词填空，将源文件中的 大写单词按序替换为输入的字符串

import re
# 打开并读取文本

file = open('oldSentence.txt', 'rt')
source = file.read()

# 使用正则表达式编译文本
pattern = re.compile(r'\b[A-Z][A-Z]+\b')  # 省略 A 为大写且单独的情况
WORD = pattern.findall(source)  # findall 方法返回一个列表 WORD

print(WORD)

for word in WORD:  # word 遍历每个 WORD 大写字母
    new_word = input('Enter an %s:\n' % word)  # 用户交互输入
    source = re.sub(word, new_word, source)  # 替换并获取每一次修改后的文本

print(source)  # 打印新文本

open('newSentence.txt', 'w').write(source)  # 把新文本写入新txt文件