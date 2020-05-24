"""
猜数游戏:
- 在程序中预设一个0~9之间的整数，让用户通过键盘输入所猜的数
- 如果大于预设的数，显示“遗憾，太大了”
- 小于预设的数，显示“遗憾，太小了”
- 如此循环，直至猜中该数，显示“预测N次，你猜中了！”
- 其中N是用户输入数字的次数
"""
import random

targetNum = random.randint(0, 9)
isCorrect = False
countGuess = 0
while not isCorrect:
    temp = int(input('猜猜看：'))
    countGuess += 1
    if temp is targetNum:
        isCorrect = True
        print('猜了{}次，终于中了！'.format(countGuess))
    elif temp > targetNum:
        print('大了！')
    else:
        print('小了！')
