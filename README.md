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

#### 循环
```

``` 



