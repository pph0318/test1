'''
    题目
    替换字符串中的空格
    example 
        input  'B C'
        output 'B??C' 
'''
def replaceBlank(inputs):
    lists = list(inputs)
    for i in range(len(lists)):
        if lists[i] == ' ':
            lists[i] = '??'
    new_strs = ''.join(lists)
    return new_strs


if __name__ == "__main__":
    strs = 'B C A '
    new = replaceBlank(strs)
    print(new)
    