"""
编写函数，模拟二分法查找
"""


def binarySearch(sourceArr, left, right, x):
    if right >= left:
        mid = int(left + (right - left) / 2)
        if sourceArr[mid] is x:
            return mid
        elif sourceArr[mid] > x:
            return binarySearch(sourceArr, left, mid - 1, x)
        else:
            return binarySearch(sourceArr, mid + 1, right, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
target = int(input('target: '))
print(binarySearch(arr, 0, len(arr) - 1, target))
