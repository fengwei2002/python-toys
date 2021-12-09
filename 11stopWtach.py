# 实现一个超级秒表

import time 

print('回车键开始应用程序，再次点击回车进行模拟物理秒表的点击，Ctrl + C 退出应用程序', end = '')

input()

print('start', end = '')

startTime = time.time() # 得到第一圈的函数

lastTime = startTime

lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 3)
        totalTime = round(time.time() - startTime, 3)

        prefixString = 'Lap #%s:' % (lapNum)
        suffixString = '%s (%s)' % (totalTime, lapTime)
        length = 14
        print(prefixString.ljust(len(prefixString) + 1) + suffixString.rjust(14), end = '')

        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    # 手动处理异常，使得控制台不打印异常
    print('\ndone')