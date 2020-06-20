"""
假设一段楼梯共15个台阶,小明一步最多能上3个台阶。
编写程序计算小明上这段楼梯一共有多少种方法。
要求给出递推法和递归法两种代码。
"""


# 递推
# https://leetcode-cn.com/problems/climbing-stairs/
def climbStairs1(stairs, maxStep):
	dp = [-1]  # dp[i] = i级台阶有多少种方法
	for i in range(1, stairs + 1):
		current = 0
		for k in range(1, maxStep+1):  # 走 1~maxStep 步
			if i - k > 0:
				current += dp[i - k]
			elif i - k == 0:
				current += 1
		dp.append(current)
	return dp[-1]


print(climbStairs1(15, 3))
