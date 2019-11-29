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