"""
羊车门问题
有3扇关闭的门，一扇门后面停着汽车，其余门后是山羊，只有主持人知道每扇门后面是什么。
参赛者可以选择一扇门，在开启它之前，主持人会开启另外一扇门，露出门后的山羊，然后允许参赛者更换自己的选择。
请问：参赛者更换选择后能否增加猜中汽车的机会？这是一个经典问题。
请使用random库对这个随机事件进行预测，分别输出参赛者改变选择和坚持选择获胜的机率。
"""
import random

TIMES = 1000
notChangeCount = 0  # 初始化不改选择的次数
changeCount = 0  # 初始化更改选择的次数
for i in range(TIMES):
    inDoor = random.randint(0, 2)
    guess = random.randint(0, 2)
    if inDoor is guess:
        notChangeCount += 1
    else:
        changeCount += 1
print("不改选择:{:.2f}%".format(notChangeCount / TIMES * 100))
print("更改选择:{:.2f}%".format(changeCount / TIMES * 100))
