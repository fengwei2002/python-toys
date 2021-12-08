import re 

phone_number_RE = re.compile(r'\d\d\d\d\d\d')

text = '142857'

match_object = phone_number_RE.search(text)

print(match_object.group()) 
# group([int]) 参数 如果是 1 就是正则表达式中的第一个括号中的内容
# 想要获取全部的分组，使用 groups 分组
a, b, c = match_object.groups()

heroRegex = re.compile(r'Batman | Tina')
mo1 = heroRegex.search('Batman and Tina')
print(mo1.group())

heroRegex = re.compile(r'Bat(man|women|mobile')

batRegex = re.compile(r'Bat(wo)?man') # 添加问号代表可选分组 
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

a = batRegex.findall(text)


