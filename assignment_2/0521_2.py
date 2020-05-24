"""
从random库中选取相应的函数满足下列条件:
 - 随机生成100内的10个整数
- 随机选取0到100间的奇数
- 从字符串 “abcdeffehij”中随机选取4个字符
- 随机选取列表［'apple', 'pear’, 'peach', ‘Grange’]中的 1 个字符串
"""
import random

# 1
print('# 1')
for a in range(1, 11):
    print(random.randrange(0, 100, 1), end=' ')
# 2
print('\n# 2')
print(random.randrange(1, 100, 2), end=' ')
# 3
print('\n# 3')
str3 = 'abcdeffehij'
randomIndexes = []
while len(randomIndexes) < 4:
    currentIndex = random.randrange(0, len(str3))
    if currentIndex not in randomIndexes:
        randomIndexes.append(currentIndex)
        print(str3[currentIndex], end=' ')
# 4
print('\n# 4')
list4 = ['apple', 'pear', 'peach', 'Grange']
print(random.choice(list4))
