import sys
import pyperclip

PASSWORDS = {
    'pw': 'guIgh2wiP95714n',
    'gmail': 'psychonaut1f@gmail.com',
    'blog': 'https://konng.vercel.app',
    'github': 'https://github.com/fengwei2002'}

if len(sys.argv) < 2:  # 如果传入的参数数量小于 2 ，那么提示用户应该输入的方式
    sys.exit()
    # print('Usage: python -u passwordCell.py [account] - To copy account password to lipboard')

account = sys.argv[1]

if account in PASSWORDS:  # 如果账户存在，就将 key 对应的 value 复制到剪切板中
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

# *.bat 中添加 @pause 暂停使用脚本之后的窗口
# 将 bat 放到 C:/windows/*.bat 即可运行脚本

# 脚本内容如下：


# @py.exe 'windows下的路径'.py %*

# @pause 或者
# exit
