"""
24点游戏是指随机选取4张扑克牌（不包括大小王），然后通过四则运算来构造表达式，
如果表达式的值恰好等于24就赢一次。
下面的代码定义了一个函数用来测试随机给定的4个数是否符合24点游戏规则，
如果符合就输出所有可能的表达式。
"""


def judgePoint24(nums):
    if not nums:
        return False

    def helper(nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    newNums = [nums[k] for k in range(len(nums)) if i != k != j]
                    if helper(newNums + [nums[i] + nums[j]]): return True
                    if helper(newNums + [nums[i] - nums[j]]): return True
                    if helper(newNums + [nums[i] * nums[j]]): return True
                    if nums[j] != 0 and helper(newNums + [nums[i] / nums[j]]):
                        return True
        return False

    return helper(nums)


input4num = input('input: ')
inputList = input4num.split(' ')
print(judgePoint24(list(map(int, inputList))))
