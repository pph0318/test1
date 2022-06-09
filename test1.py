'''
this is test,thank you!
'''
def outer(a):
    b = 10
    # inner是内函数
    def inner():
        # 在内函数中 用到了外函数的临时变量
        print(a + b)
    # 外函数的返回值是内函数的引用
    return inner
if __name__ == "__main__":
    outer(5)()
