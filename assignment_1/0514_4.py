"""
输出进度条
"""
import time

totalUnit = 43
intervalTime = 0.07

for progress in range(0, totalUnit + 1):
    strProgress = '#' * progress + '-' * (totalUnit - progress)
    print('\r{:.1f}%\t[{}]\t{:.2f}s'.format(progress * 100 / totalUnit, strProgress, progress * intervalTime), end='')
    time.sleep(intervalTime)
