### python自学教程一
### python基础语法

#### 单行定义多个变量或赋值
```
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
``` 

```
# 计算一位数码相机销售人员的工资。他的基本工资是 1500，每售出一台相机他可以得到 200 并且获得 2% 的抽成。程序要求输入相机数量及单价。
base_salary = 1500
get_rate = 200
precent_rate = 0.02
count = int(input("请输入相机的数量"))
price= int(input("请输入相机的单价"))
all_salary = base_salary + get_rate * count + precent_rate * count * price
print(all_salary)
``` 

#### if elif else 的基本语法结构。

```
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
``` 

## 循环

#### while循环
```
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

``` 

#### 列表
```
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
``` 

#### for循环
for 循环遍历任何序列（比如列表和字符串）中的每一个元素
```
# for 循环遍历任何序列（比如列表和字符串）中的每一个元素
a = ['test1', 'test2', 'test3']
for x in a:
    print(x) 

for x in a[1:2]:
    print(x)
``` 

#### range函数
```
# range函数
for i in range(5):
    print(i) #1,2,3,4,5

a = list(range(1, 5))
print(a)   #[1, 2, 3, 4]

b = list(range(1, 15, 3))
print(b)   #[1, 4, 7, 10, 13]
``` 

#### continue，break语句
break跳出循环 ，continue它会跳过其后的代码回到循环开始处执行。
```
# 我们要求用户输入一个整数，如果输入的是负数，那么我们会再次要求输入，如果输入的是整数，我们计算这个数的平方。用户输入 0 来跳出这个无限循环。
while True:
    n = int(input("input a number"))
    if n < 0:
        continue  #会返回到开始处执行
    elif n == 0:
        break     #跳出循环
    else:
        print("square is", n ** 2)

``` 

#### 循环的else语句
在循环终止完成后执行
```
# 循环的else语句（循环结束后执行）
for i in range(1, 5):
    print(i)
else:
    print('end')

```

# python 数据结构

#### 列表
```
#列表基本操作
a = [1, 2, 3, 4]
#在列表a的末尾添加元素45
a.append(45)        #在列表a的末尾添加元素45
#在列表1的位置，添加元素111
a.insert(1, 111)    #在列表1的位置，添加元素111
#列表方法 count(s) 会返回列表元素中 s 的数量。
a.count(45)         #列表方法 count(s) 会返回列表元素中 s 的数量。
#列表中移除任意的值
a.remove(3)         #列表中移除任意的值
print(a)            #[1, 111, 2, 4, 45]
#反转列表
a.reverse()         #反转列表
print(a)            #[45, 4, 2, 111, 1]
b = [321, 456, 125, 14]
#将一个列表的所有元素添加到另一个列表的末尾
a.extend(b)         #将一个列表的所有元素添加到另一个列表的末尾
print(a)            #[45, 4, 2, 111, 1, 321, 456, 125, 14]
#给列表排序
a.sort()            #给列表排序
print(a)            #[1, 2, 4, 14, 45, 111, 125, 321, 456]
#删除指定位置的元素
del a[1]            #删除指定位置的元素

``` 

#### 将列表用作栈和队列
```
# 将列表用作栈和队列

b = [1, 2, 3, 4, 5]
# pop(i), 会讲第i个元素弹出
b.pop(2)            #3
print(b)            #[1, 2, 4, 5]
``` 

#### 列表推导
```
# 列表推导
#  for 循环中的被创建（或被重写）的名为 x 的变量在循环完毕后依然存在
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)         #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 等价于
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)          #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 等价于
squares = [x ** 2 for x in range(10)]
print(squares)          #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 例如
combs = []
for x in [1, 3, 4]:
    for y in [2, 4, 6]:
        if x != y:
            combs.append((x, y))
print(combs)

# 等价于
combs = [(x, y) for x in [1, 3, 4] for y in [2, 4, 6] if x != y]
print(combs)

# 列表推导式也可以嵌套
a = [1, 2, 3]
z = [x + 1 for x in [x ** 2 for x in a]]

``` 

#### 元组
元组是由数个逗号分割的值组成, 元组是不可变类型，这意味着你不能在元组内删除或添加或编辑任何值
```
# 元组
# 元组是由数个逗号分割的值组成
# 元组是不可变类型，这意味着你不能在元组内删除或添加或编辑任何值
a = 'test1', 'test2', 'test3', 'test4'
print(a)        #('test1', 'test2', 'test3', 'test4')
print(a[1])     #test2

# 要创建只含有一个元素的元组，在值后面跟一个逗号。
a = (123)
print(a)        #123
print(type(a))  #<class 'int'>
a = (123, )
print(a)        #(123, )
print(type(a))  #<class 'tuple'>
b = 321,
print(b)        #(321, )
print(type(b))  #<class 'tuple'>
```  

#### 集合
大括号或 set() 函数可以用来创建集合。注意：想要创建空集合，你必须使用 set() 而不是 {}。  
集合对象还支持 union（联合），intersection（交），difference（差）和 symmetric difference（对称差集）等数学运算。 
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。 
```
# 集合
# 大括号或 set() 函数可以用来创建集合。注意：想要创建空集合，你必须使用 set() 而不是 {}。  
# 集合对象还支持 union（联合），intersection（交），difference（差）和 symmetric difference（对称差集）等数学运算。 
# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。

test = {'pink', 'red', 'green', 'white'}
print(type(test))       # <class 'set'>
print('pink' in test)   # True
print('blank' in test)  # False

# 对俩个单词中的字母进行集合操作
a = set('abcdefghijk')
b = set('hijkmlnopq')
# a中集合减去b中集合（在a集合中去掉和b相同的元素）
print(a - b)            # {'g', 'f', 'e', 'a', 'c', 'b', 'd'}
# a和b集合的合并
print(a | b)            # {'e', 'l', 'o', 'g', 'd', 'q', 'i', 'b', 'c', 'h', 'n', 'k', 'm', 'f', 'p', 'j', 'a'}
# a集合和b集合的并集
print(a & b)            # {'i', 'h', 'j', 'k'}
# 去掉a集合和b集合的并集，并合并a集合和b集合
print(a ^ b)            # {'e', 'l', 'n', 'm', 'o', 'g', 'f', 'p', 'q', 'd', 'a', 'b', 'c'}
# 从集合中添加或者弹出集合
print(a.pop())          # g
a.add('l')       
print(a)                # {'c', 'g', 'i', 'd', 'e', 'f', 'a', 'j', 'k', 'l', 'b'}
``` 


