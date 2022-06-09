'''
二维数组中的查找
给定一个二维数组，其每一行从左到右递增排序，从上到下也是递增排序。给定一个数，判断这个数是否在该二维数组中。
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''
from asyncio.windows_events import NULL


def getIn(matrix,finds):
    if len(matrix) == 0 or matrix == NULL or len(matrix[0]) == 0:
        return False
    rows,cols = len(matrix),len(matrix[0])
    r,c = 0,cols - 1 
    while(r <= rows - 1 and c >= 0):
        if matrix[r][c] == finds:
            return True
        elif matrix[r][c] < finds:
            r+=1
        else:
            c-=1
    return False
    pass

if __name__ == '__main__':
    lists = [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ]
# 回忆遍历二维数组
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            print(lists[i][j],end='\t')
        print('\n')
    print(getIn(lists,31))
