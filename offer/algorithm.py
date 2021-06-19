"""
冒泡排序
"""


def bubble(arr):
    if len(arr) < 2:
        return
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


list1 = [33, 45, 3, 45, 7, 89, 3, 2, 46, 1, 99]
bubble(list1)
print(list1)