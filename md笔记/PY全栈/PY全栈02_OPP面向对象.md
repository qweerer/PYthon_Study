# OO(ObjectOriented)面型对象

## 1.面向对象的概念

- OO:面向对象
- OOA:面向对象分析
- OOD:面向对象设计
- OOI:面向对象实现
- OOP:面向对象编程

## 2.什么是面向对象

>接触到任意一个任务,首先想到的是任务的世界构成,是构成模型的名词.
>就像上帝创造世界一样,先加入太阳,水,生物这些物体,然后决定这些物体的运作

## 3.python面相对象要学什么

- 面向对象编程
  - 基础
  - 共有私有
  - 继承
  - 组合, Mixin
- 魔法函数
  - 魔法函数概述
  - 构造魔法函数
  - 运算魔法函数

## 3.类与对象

### 区别

- 类:抽象名词,代表一个集合,具有共性的事物
- 对象:具体的事物,具体到每个个体

### 类的内容

- 函数:成员的方法,表名事物的功能或者属性
- 变量:一类事物的属性,表名事物的特征

### 创建类

- 类的命名:
  - 与变量相同的驼峰命名方法
- 类的声明
  - 使用`class`
  - 案例:'./代码案例/PY全栈02_OPP面向对象.py'1.1-1.3
- 访问对象成员检查

        obj.__dict__
        # dict前后有两个下划线

### self

> 类中函数自动带一个变量`self`
> 案例: `./代码案例/PY全栈02_OPP面向对象.py` 1.4

```python
class student():

    name = None
    age = 18
    gender = 'man'
    course = 'Python'

    # 这个函数必须有(self)的变量传入
    def doHomeWork(self):
        self.name = '1110k'
        print(self.name,end=' ')
        print('正在做作业')
        return None
stu_xiaoming = student()
stu_xiaoming.doHomeWork()
print(stu_xiaoming.name)
```

- 如果不加`self`则成为一个类的函数,
  - 他的调用为:

        类名.函数名()
  - 访问类的变量方法为:

        __class__.变量名

```python
class student():

    name = None
    age = 18
    gender = 'man'
    course = 'Python'

    def doHomeWorkagain():
        print('正在做作业')
        print(__class__.name)
        print(__class__.age)
        return None



student.doHomeWorkagain()
```

```python
正在做作业
None
18
```

### 鸭子模型

> 不论是否是本类,只要构造相同,就可以调用

```python
class A():
    name = " liuying"
    age = 18

    def __init__(self):
        self.name = "aaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbb"
    age = 90

a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()

# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)

# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)
```

    aaaa
    200
    aaaa
    200
    liuying
    18
    bbbb
    90

## 4. 面向对象的三大特性

- 封装
- 继承
- 多态

### 4.1 封装

- 封装就是对对象的成员进行访问限制
- 封装的三个级别：
  - 公开，public
  - 受保护的，protected
  - 私有的，private
  - public，private，protected不是关键字
- 判别对象的位置
  - 对象内部
  - 对象外部
  - 子类中
- [python中下划线使用](http://blog.csdn.net/handsomekang/article/details/40303207)
- 私有
  - 私有成员是最高级别的封装，只能在当前类或对象中访问
  - 在成员前面添加两个两个下划线即可

        class Person():
            # name是共有的成员
            name = "liuying"
            # __age就是私有成员
            __age = 18
    > Python的私有不是真私有，是一种成为name mangling的改名策略
    > 可以使用对象._classname_attributename访问
- 受保护的封装  protected
  - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者子类中都
  可以进行访问，但是在外部不可以
  - 封装方法： 在成员名称前只加一个下划线即可
- 公开的，公共的 public
  - 公共的封装实际对成员没有任何操作，任何地方都可以访问