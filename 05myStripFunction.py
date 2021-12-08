# 使用正则表达式实现 strip 函数
# 去除传入字符串的左右的多余空格

import re 

parameter1 = input('原始字符串：')
parameter2 = input('要删除的字符：回车跳过这一步')

# \s 相当简单是许多正则表达式中 “任何空白字符” 的常见简写。这包括空格、制表符和换行符。
def func(origin, parameter2):
    basicRegex = re.compile(r'^\s*|\s*$')
    # ^代表必须以这个参数开始 $代表必须以这个参数结束
    parameter2Regex = re.compile(parameter2)

    if parameter2 == '':
        print(basicRegex.sub('', origin)) # re.sub用于替换字符串中的匹配项
        # print re.sub(r'\s+', '-', text) 将 text 中的空格替换为 '-'
    else:
        print(parameter2Regex.sub('', origin))


func(parameter1, parameter2)