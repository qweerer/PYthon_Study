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

### 3.1 区别

- 类:抽象名词,代表一个集合,具有共性的事物
- 对象:具体的事物,具体到每个个体

### 3.2 类的内容

- 函数:成员的方法,表名事物的功能或者属性
- 变量:一类事物的属性,表名事物的特征

### 3.3 创建类

- 类的命名:
  - 与变量相同的驼峰命名方法
- 类的声明
  - 使用`class`
  - 案例:'./代码案例/PY全栈02_OPP面向对象.py'1.1-1.3
- `访问对象成员检查`

        obj.__dict__
        # dict前后有两个下划线

### 3.4 self

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

    ```python
    print(Person.__dict__)
    ```

    > 将`Person`的所有实例打印出来,会发现一个叫做`'_Person__age':18`的实例,这个就是`__age=18`真正的名字

    ```c
    mappingproxy({'__module__': '__main__',
                'name': 'liuying',
                '_Person__age': 18,
                '__dict__': <attribute '__dict__' of 'Person' objects>,
                '__weakref__': <attribute '__weakref__' of 'Person' objects>,
                '__doc__': None})
    ```

- 受保护的封装  protected
  - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者子类中都可以进行访问，但是在外部不可以
  - 封装方法： 在成员名称前只加一个下划线即可
- 公开的，公共的 public
  - 公共的封装实际对成员没有任何操作，任何地方都可以访问

### 4.2 继承

- 继承就是一个类可以获得另外一个类中的成员属性和成员方法
- 作用： 减少代码，增加代码的复用功能， 同时可以设置类与类直接的关系
- 继承与被继承的概念：
  - 被继承的类叫父类，也叫基类，也叫超类
  - 用于继承的类，叫子类，也叫派生类
  - 继承与被继承一定存在一个 is-a 关系
- 继承的语法，参见oop-2.ipynb
- 继承的特征
  - 所有的类都继承自object类，即所有的类都是object类的子类
  - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
  - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
  - 子类中可以定义独有的成员属性和方法
  - 子类中定义的成员和父类成员如果相同，则优先使用子类成员
  - 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，可以使用 [父类名.父类成员] 的格式来调用父类成员，也可以使用super().父类成员的格式来调用
- 继承变量函数的查找顺序问题
  - 优先查找自己的变量
  - 没有则查找父类
  - 构造函数如果本类中没有定义，则自动查找调用父类构造函数
  - 如果本类有定义，则不在继续向上查找
- 构造函数
  - 是一类特殊的函数，在类进行实例化之前进行调用
  - 如果定义了构造函数，则实例化时使用构造函数，不查找父类构造函数
  - 如果没定义，则自动查找父类构造函数
  - 如果子类没定义，父类的构造函数带参数，则构造对象时的参数应该按父类参数构造
- super
  - super不是关键字， 而是一个类
  - super的作用是获取MRO（MethodResolustionOrder）列表中的第一个类
  - super于父类直接没任何实质性关系，但通过super可以调用到父类
  - super使用两个方,参见在构造函数中调用父类的构造函数

- 单继承和多继承
  - 单继承：每个类只能继承一个类
  - 多继承，每个类允许继承多个类

- 单继承和多继承的优缺点
  - 单继承：
  - 传承有序逻辑清晰语法简单隐患少呀
    - 功能不能无限扩展，只能在当前唯一的继承链中扩展
  - 多继承：
    - 优点：类的功能扩展方便
    - 缺点：继承关系混乱

- 菱形继承/钻石继承问题
  - 多个子类继承自同一个父类，这些子类由被同一个类继承，于是继承关系图形成一个菱形图谱
  - [MRO](https://www.cnblogs.com/whatisfantasy/p/6046991.html)
  - 关于多继承的MRO
    - MRO就是多继承中，用于保存继承顺序的一个列表
    - python本身采用C3算法来多多继承的菱形继承进行计算的结果
    - MRO列表的计算原则：
      - 子类永远在父类前面
      - 如果多个父类，则根据继承语法中括号内类的书写顺序存放
      - 如果多个类继承了同一个父类，孙子类中只会选取继承语法括号中第一个父类的父类

- 构造函数
  - 在对象进行实例化的时候，系统自动调用的一个函数叫构造函数，通常此函数用来对实例对象进行初始化，顾名
  - 构造函数一定要有，如果没有，则自动向上查找，按照MRO顺序，直到找到为止

## 3.3 多态
- 多态就是同一个对象在不同情况下有不同的状态出现
- 多态不是语法，是一种设计思想
- 多态性： 一种调用方式，不同的执行效果
- 多态： 同一事物的多种形态，动物分为人类，狗类，猪类
- [多态和多态性](https://www.cnblogs.com/luchuangao/p/6739557.html)

- Mixin设计模式
    - 主要采用多继承方式对类的功能进行扩展
    - [Mixin概念](https://www.zhihu.com/question/20778853)
    - [MRO and Mixin](http://blog.csdn.net/robinjwong/article/details/48375833)
    - [Mixin模式](https://www.cnblogs.com/xybaby/p/6484262.html)
    - [Mixin MRO](http://runforever.github.io/2014-07-19/2014-07-19-python-mixin%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)
    - [MRO](http://xiaocong.github.io/blog/2012/06/13/python-mixin-and-mro/)
    
- 我们使用多继承语法来实现Minxin
- 使用Mixin实现多继承的时候非常小心
    - 首先他必须表示某一单一功能，而不是某个物品
    - 职责必须单一，如果由多个功能，则写多个Mixin
    - Mixin不能依赖于子类的实现
    - 子类及时没有继承这个Mixin类， 也能照样工作，只是缺少了某个功能
- 优点
    - 使用Mixin可以在不对类进行任何修改的情况下，扩充功能
    - 可以方便的组织和维护不同功能组件的划分
    - 可以根据需要任意调整功能类的组合
    - 可以避免创建很多新的类，导致类的继承混乱
