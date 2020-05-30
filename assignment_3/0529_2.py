"""
编写函数，模拟选择法排序
"""


def selectionSort(sourceArray):
    for index in range(0, len(sourceArray)):
        currentMin = index  # 当前遍历中最小值的游标，初始化
        for currentIndex in range(index + 1, len(sourceArray)):
            if sourceArray[currentIndex] < sourceArray[currentMin]:
                currentMin = currentIndex
        # 单次遍历结束，按下标交换值
        sourceArray[index], sourceArray[currentMin] = sourceArray[currentMin], sourceArray[index]


targetArray = [7, 6, 1, 1, 5, 1, 2]
selectionSort(targetArray)
print(targetArray)
