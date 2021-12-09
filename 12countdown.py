# 一个简单的倒计时程序

import time
import subprocess

timeLeft = int(input('countdown.py -: please input a second number '))

while timeLeft > 0:
    time.sleep(1)
    if timeLeft == 1:
        print(timeLeft, end = '\n')
        print('break time is over')
    else:
        print(timeLeft, end = ' > ')
    timeLeft = timeLeft - 1

# 结束应用程序之后，输出结束的图案， 或者播放声音
# subprocess.Popen(['start', 'end.mp3'], shell=True)