"""
输出进度条
"""
import time
for progress in range(0, 26):
    strProgress = '#' * progress + '-' * (25 - progress)
    print('\r{}%\t[{}]'.format(progress * 4, strProgress), end='')
    time.sleep(0.1)
