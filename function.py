# # 使用关键字来定义一个函数
# # 我们使用关键字 def 来定义一个函数
# # def 函数名(参数):
# #     语句1
# #     语句2
# def sum(a,b):
#     return a + b
# print(sum(2, 3))

# # 局域或全局变量
# def change():
#     a = 90
#     print(a)
# a = 9
# print("Before the function call ", a)
# print("inside change function", end=' ')
# change()
# print("After the function call ", a)
# # 首先我们对 a 赋值 9，然后调用更改函数，这个函数里我们对 a 赋值 90，然后打印 a 的值。调用函数后我们再次打印 a 的值。
# # 当我们在函数里写 a = 90 时，它实际上创建了一个新的名为 a 的局部变量，这个变量只在函数里可用，并且会在函数完成时销毁。所以即使这两个变量的名字都相同，但事实上他们并不是同一个变量。 

# # 可以直接打印输出 9。
# a = 9
# def change1():
#     print(a)    # 9
# change1()

# # 原因是当函数中只要用到了变量 a，并且 a 出现在表达式等于号的前面，就会被当作局部变量。当执行到 print(a) 的时候会报错，因为 a 作为函数局部变量是在 print(a) 之后才定义的。
# a = 9
# def change2():
#     print(a)    #“UnboundLocalError: local variable 'a' referenced before assignment”
#     a = 100
# change2()

# # 使用 global 关键字，对函数中的 a 标志为全局变量，让函数内部使用全局变量的 a
# a = 9
# def change():
#     global a
#     print(a)
#     a = 100
#     print(a)
# change()

# #程序中的 end=' ' 参数表示，print 打印后的结尾不用换行，而用空格。默认情况下 print 打印后会在结尾换行
# a = 9
# def change():
#     global a
#     print(a)
#     a = 100
# print("Before the function call ", a)
# print("inside change function", end=' ')
# change()
# print("After the function call ", a)

# # 默认参数值
# # 调用者未给出 b 的值，那么 b 的值默认为 99
# def test(a, b = 99):
#     if a > b:
#         return True
#     else:
#         return False
# print(test(1000))
# print(test(20))

# # 是具有默认值的参数后面不能再有普通参数，比如 f(a,b=90,c) 就是错误的。
# # 默认值只被赋值一次，因此如果默认值是任何可变对象时会有所不同
# def f(a, b = []):
#     b.append(a)
#     return b
# print(f(1))     #[1]
# print(f(2))     #[1, 2]

# def f(a, data = []):
#     if data is None:
#         data = []
#     data.append(a)
#     return data
# print(f(1))     #[1]
# print(f(2))     #[1, 2]
# print(f(4, [])) #[4]


# # 高阶函数
# # 创建一个函数，将参数列表中每个元素都变成全大写
# def high(l):
#     return [i.upper() for i in l]
# print(high(['er', 'sdt', 'erf']))   #['ER', 'SDT', 'ERF']

# # 创建高阶函数，接受一个函数和一个列表作为参数
# def test(h, l):
#     return h(l)
# l = ['er', 'sdt', 'erf']
# print(test(high, l))    #['ER', 'SDT', 'ERF']

# # map函数
# # map 是一个在 Python 里非常有用的高阶函数。它接受一个函数和一个序列（迭代器）作为输入，然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结果。
# lst = [1, 2, 3, 4, 5]
# def square(num):
#     return num * num
# print(list(map(square, lst)))   #[1, 4, 9, 16, 25]

# # 文件操作
# # 我们使用 open() 函数打开文件。它需要两个参数，第一个参数是文件路径或文件名，第二个是文件的打开模式。
# # "r"，以只读模式打开，你只能读取文件但不能编辑/删除文件的任何内容
# # "w"，以写入模式打开，如果文件存在将会删除里面的所有内容，然后打开这个文件进行写入
# # "a"，以追加模式打开，写入到文件中的任何数据将自动添加到末尾 

# # 文件读取
# f = open('README.md')
# print(f)        #<_io.TextIOWrapper name='README.md' mode='r' encoding='UTF-8'>
# # readline() 能帮助你每次读取文件的一行。
# print(f.readline())
# print(f.readline())
# # 使用 read() 方法一次性读取整个文件。
# # 如果你再一次调用 read()，它会返回空字符串因为它已经读取完整个文件。
# # read(size) 有一个可选的参数 size，用于指定字符串长度。如果没有指定 size 或者指定为负数，就会读取并返回整个文件。当文件大小为当前机器内存两倍时，就会产生问题。反之，会尽可能按比较大的 size 读取和返回数据。
# print(f.read())

# # 打开文件后我们应该总是关闭文件。我们使用方法 close() 完成这个操作。
# f.close()

# # 文件写入
# f = open('README.md')
# f.write('测试1\n')  #io.UnsupportedOperation: not writable
# f.write('ceshi2\n') #io.UnsupportedOperation: not writable

# # 拷贝文件
# import sys
# if len(sys.argv) < 3:
#     print("Wrong parameter")
#     print("./copyfile.py file1 file2")
#     sys.exit(1)
# f1 = open(sys.argv[1])
# s = f1.read()
# f1.close()
# f2 = open(sys.argv[2], 'w')
# f2.write(s)
# f2.close()

# 文本文件相关信息统计
import os
import sys
def parse_file(path):
    ""
    分析给定文本文件，返回其空格、制表符、行的相关信息

    :arg path: 要分析的文本文件的路径

    :return: 包含空格数、制表符数、行数的元组
    ""