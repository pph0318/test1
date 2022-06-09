if __name__ == '__main__':
    run = {
        "i": {
            "title": "交互式编程( Interactive )",
            "desc": [
                "打开终端，输入 python 回车",
                "进入 Python 交互式命令行",
                "输入 print('monkey king is coding!')"
            ]
        },
        "f": {
            "title": "Python 源代源文件( File )",
            "desc": [
                "使用你喜欢的编辑器拷贝本练习的代码, 保存为run.py",
                "打开终端，cd 到 run.py 保存的目录",
                "输入 python run.py"
            ]
        }
    }
 
    print("有两种基本的方式运行 Python")
    for s in run:
        print(s)
        item = run.get(s)
        print("* {}: {}".format(s, item['title']))
 
    has_learn_i = False
    has_learn_f = False
 
    # TODO(You): 请在此实现代码
 
    if has_learn_i and has_learn_f:
        print("[2/2]您已完成两种 Python 运行方式的学习")
    elif has_learn_f:
        print("[1/2]您已完成 Python 源代码方式运行学习")
    elif has_learn_i:
        print("[1/2]您已完成 Python 交互式命令行运行学习")
    else:
        print("[0/2]您似乎跳过了运行方式的学习？期待下次光临！")