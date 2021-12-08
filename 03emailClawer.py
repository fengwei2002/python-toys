import pyperclip
import re


# konng0102@gmail.com
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # 用户名字的所有种类
    @ #                 @ 邮箱符号
    [a-zA-Z0-9.-]+      # 域名
    (\.[a-zA-Z]{2,4})   # 域名后缀
)''', re.VERBOSE)


text = str(pyperclip.paste())
# 将剪切板中的数据转到 text 中


matches = [] 
# 开辟数组

for email in emailRegex.findall(text):
    matches.append(email)
# 对于 text 使用 emailRegex 进行遍历
# 将 email 都累加到 matches 中


# 如果找到了符合条件的 email，就将这部分数据抄到 pyperclip 中，
# 同时控制台进行数据输出
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

