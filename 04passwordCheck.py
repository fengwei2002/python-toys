# 强口令检查的正则
# 用来判断用户的输入是不是一个强口令

# 长度不小于 8 个字符， 同时包含大写和小写字符，至少包含一个数字

import re, pyperclip

text = str(pyperclip.paste())

def check(text):
    if len(text) <= 8:
        print("Not satisfied")
        return False
    numberRegex = re.compile(r'\d+')

    if numberRegex.search(text) == None:
        print("Not satisfied")
        return False

    lowerLetterRegex = re.compile(r'[a-z]+')

    if lowerLetterRegex.search(text) == None:
        print("Not satisfied")
        return False

    upperLetterRegex = re.compile(r'[A-Z]+')

    if upperLetterRegex.search(text) == None:
        print("Not satisfied")
        return False

print(check(text))