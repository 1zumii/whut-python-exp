"""
编写函数，使用递归算法实现冒泡排序算法
"""


def cocktailSort(arr):
    orderArr = [True]  # 基本数据类型没有引用
    indexStart, indexEnd = 0, len(arr) - 1  # 未排序的部分
    while indexEnd - indexStart > 0:
        order = orderArr[0]
        if order:  # 正序冒泡
            rangeStart, rangeEnd, stepLength = indexStart, indexEnd, 1
        else:  # 逆序冒泡
            rangeStart, rangeEnd, stepLength = indexEnd, indexStart, -1
        for index in range(rangeStart, rangeEnd, stepLength):
            if order and arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
            elif not order and arr[index] < arr[index - 1]:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
        if order:
            indexEnd -= 1
        else:
            indexStart += 1
        orderArr[0] = not order


targetArray = [7, 6, 1, 1, 5, 1, 2]
cocktailSort(targetArray)
print(targetArray)
