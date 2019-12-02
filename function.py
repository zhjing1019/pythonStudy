# 使用关键字来定义一个函数
# 我们使用关键字 def 来定义一个函数
# def 函数名(参数):
#     语句1
#     语句2
def sum(a,b):
    return a + b
print(sum(2, 3))

# 局域或全局变量
def change():
    a = 90
    print(a)
a = 9
print("Before the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)
# 首先我们对 a 赋值 9，然后调用更改函数，这个函数里我们对 a 赋值 90，然后打印 a 的值。调用函数后我们再次打印 a 的值。
# 当我们在函数里写 a = 90 时，它实际上创建了一个新的名为 a 的局部变量，这个变量只在函数里可用，并且会在函数完成时销毁。所以即使这两个变量的名字都相同，但事实上他们并不是同一个变量。 

# 可以直接打印输出 9。
a = 9
def change1():
    print(a)    # 9
change1()

# 原因是当函数中只要用到了变量 a，并且 a 出现在表达式等于号的前面，就会被当作局部变量。当执行到 print(a) 的时候会报错，因为 a 作为函数局部变量是在 print(a) 之后才定义的。
a = 9
def change2():
    print(a)    #“UnboundLocalError: local variable 'a' referenced before assignment”
    a = 100
change2()

# 使用 global 关键字，对函数中的 a 标志为全局变量，让函数内部使用全局变量的 a
a = 9
def change():
    global a
    print(a)
    a = 100
    print(a)
change()

#程序中的 end=' ' 参数表示，print 打印后的结尾不用换行，而用空格。默认情况下 print 打印后会在结尾换行
a = 9
def change():
    global a
    print(a)
    a = 100
print("Before the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)

# 默认参数值
# 调用者未给出 b 的值，那么 b 的值默认为 99
def test(a, b = 99):
    if a > b:
        return True
    else:
        return False
print(test(1000))
print(test(20))

# 是具有默认值的参数后面不能再有普通参数，比如 f(a,b=90,c) 就是错误的。
# 默认值只被赋值一次，因此如果默认值是任何可变对象时会有所不同
def f(a, b = []):
    b.append(a)
    return b
print(f(1))     #[1]
print(f(2))     #[1, 2]

def f(a, data = []):
    if data is None:
        data = []
    data.append(a)
    return data
print(f(1))     #[1]
print(f(2))     #[1, 2]
print(f(4, [])) #[4]


# 高阶函数
# 创建一个函数，将参数列表中每个元素都变成全大写
def high(l):
    return [i.upper() for i in l]
print(high(['er', 'sdt', 'erf']))   #['ER', 'SDT', 'ERF']

# 创建高阶函数，接受一个函数和一个列表作为参数
def test(h, l):
    return h(l)
l = ['er', 'sdt', 'erf']
print(test(high, l))    #['ER', 'SDT', 'ERF']