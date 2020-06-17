"""
尼姆游戏是个著名的游戏,有很多变种玩法。
两个玩家轮流从一堆物品中拿走一部分；
在每一步中，玩家可以自由选择拿走多少物品,但是必须至少拿走一个并且最多只能拿走一半物品，然后轮到下一个玩家。
拿走最后一个物品的玩家输掉游戏。
在聪明模式中，计算机每次拿走足够多的物品使得堆的大小是2的幂次方减1——也就是3,7,15,31或63。
除了堆的大小已经是2的幂次方减1，在其他情况下这样走都是符合游戏规则的。
在那种情况下,计算机就按游戏规则随机拿走一些。
编写程序,模拟聪明版本的尼姆游戏。
"""
import math
import random


def checkTake(take, remain):
	if take < 1:
		return False
	if remain > 1:
		return take <= remain // 2
	else:
		return take is 1


def Nimes(n, isFirst):
	remain = n
	if isFirst:
		playerTake = int(input('剩余 {} 个，拿：'.format(remain)))
		if not checkTake(playerTake, remain):
			print('拿取数量违反规则')
			return
		remain -= playerTake
		if remain is 0:
			print('电脑赢了！你输了！')
			return
	while remain > 0:
		# 电脑拿
		if math.log(remain + 1, 2) % 1 == 0:
			# 除了堆的大小已经是2的幂次方减1，此时计算机就按游戏规则随机拿走一些
			if remain is 1:
				computerTake = 1
			else:
				computerTake = random.choice(range(1, remain // 2 + 1, 1))
		else:
			# 计算机每次拿走足够多的物品使得堆的大小是2的幂次方减1
			if remain is 2:
				computerTake = 1
			else:
				k = math.ceil(math.log(remain / 2 - 1, 2))
				computerTake = remain - pow(2, k) + 1
		print('电脑拿了 {} 个'.format(computerTake))
		remain -= computerTake
		if remain is 0:
			print('电脑输了，你赢了！')
			break
		# 玩家拿
		playerTake = int(input('剩余 {} 个，拿：'.format(remain)))
		if not checkTake(playerTake, remain):
			print('拿取数量违反规则')
			break
		remain -= playerTake
		if remain is 0:
			print('电脑赢了！你输了！')
			break


firstPlay = input("先手？(y/n) ")
if firstPlay in ['Y', 'y']:
	Nimes(random.randrange(1, 999), True)
elif firstPlay in ['N', 'n']:
	Nimes(random.randrange(1, 999), False)
else:
	print('Error: invalid input')
