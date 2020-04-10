""" 
二分查找法：
mid=[(low+high)/2]
考虑三种情况：
1.目标值=mid，查找成功；
2.目标值<mid，对前半部分序列重复这一过程，即索引的范围从low到mid-1；
3.目标值>mid，对后半部分序列重复这一过程，即索引的范围从mid-1到high；

该算法的时间复杂度是O(log(n))(线性的时间)
"""

# 二分查找的递归算法


def binary_search(data, target, low, high):
    """ 
    data：顺序列表
    target:要查找的数据
    low：最小索引
    high：最大索引
    """
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

# 二分查找的非递归算法


def binary_search2(data, target):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False


if __name__ == "__main__":
    list = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    result = binary_search(list, 22, 0, len(list)-1)
    result1 = binary_search2(list, 22)
    print(result, result1)
