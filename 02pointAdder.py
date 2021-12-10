# 将剪切板中的每一行文字的前面添加 一个星号，用于 Markdown 的快速书写

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)