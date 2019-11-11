# 单行定义多个变量或赋值
a, b = 1, 2

# 交换俩个值的数值
a, b = b, a

# 单行定义多个变量或赋值可用于元组拆分
data = ('test1', 'test2', 'test3')
nameOne, nameTwo, nameThree = data
print(nameOne)
# test1
print(nameTwo)
# test2
print(nameThree)
# test3


# 计算一位数码相机销售人员的工资。他的基本工资是 1500，每售出一台相机他可以得到 200 并且获得 2% 的抽成。程序要求输入相机数量及单价。
base_salary = 1500
get_rate = 200
precent_rate = 0.02
count = int(input("请输入相机的数量"))
price= int(input("请输入相机的单价"))
all_salary = base_salary + get_rate * count + precent_rate * count * price
print(all_salary)


#if elif else 的基本语法结构。

# if语句
num = int(input('input your num!'))
if num < 100:
    print("输入的数字小于100")

# else语句
number = int(input('input your num!'))
if number < 100:
    print("输入的数字小于100")
else:
    print("输入的数字大于100")

# elif语句
count = int(input("input your count"))
if count == 0:
    print("输入0")
elif count == 1:
    print("输入1")
elif count == 2:
    print("输入2")
else:
    print("输入其他的数字")

# 循环
# while循环
n = 0
while n < 11:
    print(n)
    n += 1

# 打印斐波那契数列
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b

# 打印10以内的乘法表
i = 1
print("-" * 50)
while i < 11:
    n  = 1
    while n <= 10:
        print("{:5d}".format(i * n), end = '')
        n += 1
    print()
    i +=1
print("-" * 50)

# 列表的数据结构
a = [1, 324, 6, 9, 10]
print(a[1])   #可以通过索引访问列表中的值
print(a[-3])  #如果我们使用负数的索引，那将会从列表的末尾开始计数
print(a[1:3]) #可以通过冒号，把索引切成不同的部分
print(a[:-2]) #省略的第一个索引默认为零
print(a[-4:]) #省略的第二个索引默认为切片的字符串的大小
print(a[1::2])  #切片操作还可以设置步长,它的意思是，从切片索引 1 到列表末尾，每隔两个元素取值。

b = a + [3, 4, 5, 6, 7]
print(b)
b[3] = 64  #可以直接修改列表
b[1:3] = [111, 222, 333]   #可以直接切片赋值