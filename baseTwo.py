# python 数据结构

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
#遍历列表的时候，获得列表的索引值enumerate()
for i, j in enumerate(['test1', 'test2']):
    print("{} in {}".format(i, j))
#同时遍历俩个序列，zip()
a = ['test1', 'test2']
b = ['test3', 'test4']
for x, y in zip(a, b):
    print("{} in {}".format(i, j))

b = [1, 2, 3, 4, 5]
# pop(i), 会讲第i个元素弹出
b.pop(2)            #3
print(b)            #[1, 2, 4, 5]

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

# 字典
# 字典是是无序的键值对（key:value）集合，同一个字典内的键必须是互不相同的。
# 一对大括号 {} 创建一个空字典。初始化字典时，在大括号内放置一组逗号分隔的键：值对，这也是字典输出的方式。我们使用键来检索存储在字典中的数据。
data = {"one": 'test1', "two": "test2", "three": "test3"}
print(data['one'])          #test1
# 创建新的键值对
data['four'] = 'test4'
# 使用 del 关键字删除任意指定的键值对
del data['two']
print(data)                 #{'one': 'test1', 'three': 'test3', 'four': 'test4'}
# 字典中的键必须是不可变类型，比如你不能使用列表作为键。

# dict() 可以从包含键值对的元组中创建字典。
b = dict((('one', 'test1'), ('two', 'test2')))
print(b)                    #{'one': 'test1', 'two': 'test2'}
# items()遍历字典
for x, y in data.items():
    print("{} use {}".format(x, y)) #one use test1   three use test3   four use test4

# dict.setdefault(key, default)
# 往字典里添加数据时，先判断字典里是否存在这个元素，不存在则创建一个默认值
data = {}
data.setdefault('name', []).append('Ruby')
print(data)         # {'name': ['Ruby']}
data.setdefault('name', []).append('python')
print(data)         # {'name': ['Ruby', 'python']}

# 试图索引一个不存在的键将会抛出一个 keyError 错误。我们可以使用 dict.get(key, default) 来索引键，如果键不存在，那么返回指定的 default 值。
print(data['foo'])  # KeyError: 'foo'


