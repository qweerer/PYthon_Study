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

- 面向对象的基础_类与对象的概念
- 面向兑现3大特性
  - 共有私有
  - 继承
  - 组合
  - 多态,Mixin
- 类的相关函数与属性
  - 成员描述
  - 内置属性
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

- 继承语法

  ```python
  class 子类名(父类名):
      pass
  ```

  案例:

  ```python
  class Person():
    name = "NoName"
    age = 18
    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = "sec" #小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("Sleeping ... ...")

  #父类写在括号内
  class Teacher(Person):
      teacher_id = "9527"
      def make_test(self):
          print("attention")

  t = Teacher()
  print(t.name)
  # 受保护不能外部访问，为啥这里可以
  print(t._petname)

  # 私有访问问题
  # 公开访问私有变量，报错
  #print(t.__score)

  t.sleep()
  print(t.teacher_id)
  t.make_test()
  ```

  >- 子类和父类定义同一个名称变量，则优先使用子类本身
  >- 子类不能使用父类中的私有成员
  >- 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
  >- 所有的类都继承自object类，即所有的类都是object类的子类

- 扩充父类函数

  >子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，可以使用 [父类名.父类成员] 的格式来调用父类成员，也可以使用super().父类成员的格式来调用

  ```python
  class Person():
      name = "NoName"
      age = 18
      __score = 0 # 考试成绩是秘密，只要自己知道
      _petname = "sec" #小名，是保护的，子类可以用，但不能公用
      def sleep(self):
          print("Sleeping ... ...")
      def work(self):
          print("make some money")

  #父类写在括号内
  class Teacher(Person):
      teacher_id = "9527"
      name = "DaNa"
      def make_test(self):
          print("attention")

      def work(self):
          # 扩充父类的功能只需要调用父类相应的函数
          Person.work(self)
          # 扩充父类的另一种方法
          # super代表得到父类
          # super()可以向上一直查找,知道找到`work()`函数为止
          super().work()
          self.make_test()

  t = Teacher()
  t.work()
  ```

  ```c
  make some money
  make some money
  attention
  ```

- 构造函数
  - 构造函数如果本类中没有定义，则自动查找调用父类构造函数,如果有，则不在继续向上查找
  - 是一类特殊的函数，在类进行实例化之前进行调用
  - 如果定义了构造函数，则实例化时使用构造函数，不查找父类构造函数
  - 如果没定义，则自动查找父类构造函数
  - 如果子类没定义，父类的构造函数带参数，则构造对象时的参数应该按父类参数构造
  - 对父构造函数的补充与普通函数的补充一致

  ```python
  class Animel():
    def __init__(self):
        print("Animel")

  class PaxingAni(Animel):
      def __init__(self, name):
          print(" Paxing Dongwu {0}".format(name))

  class Dog(PaxingAni):
      # __init__就是构造函数
      # 每次实例化的时候，第一个被自动的调用
      # 因为主要工作是进行初始化，所以得名
      def __init__(self):
          print("I am init in dog")

  # 实例化Dog时，查找到Dog的构造函数，参数匹配，不报错
  d = Dog()

  class Cat(PaxingAni):
      pass

  # 此时，由于Cat没有构造函数，则向上查找
  # 因为PaxingAni的构造函数需要两个参数，
  # 实例化的时候需要再填入一个变量,当做'PaxingAni'构造函数中的'name传入变量',
  # 否则报错
  c = Cat(123)
  ```

  ```c
  I am init in dog
  Paxing Dongwu 123
  ```

- `.__mro__`:显示家谱

  ```python
  class A():
    pass
  class B(A):
    pass
  print(A.__mro__)
  print(B.__mro__)
  ```

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

### 4.3 多态

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

## 5.类的相关函数与属性

### 5.1类相关函数

| 函数名             | 作用                                         |
| ------------------ | -------------------------------------------- |
| issubclass(B, A)   | 检测一个类(`B`)是否是另一个类(`A`)的子类     |
| isinstance(a, A)   | 检测一个对象(`a=A()`)是否是一个类(`A`)的实例 |
| hasattr(a, 'name') | 检测一个对象(`a`)是否有成员xxx(`'name'`)     |
| getattr            | get attribute                                |
| setattr            | set attribute                                |
| delattr            | delete attribute                             |
| dir(a)             | 获取对象(`a`)的成员列表                      |

### 5.2 类的成员描述符（属性）

- 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
  - get： 获取属性的操作
  - set：修改或者添加属性操作
  - delete： 删除属性的操作
- 如果想使用类的成员描述符，大概有三种方法
  - **使用类实现描述器**(不知道)
  - **使用属性修饰符**(不知道)
  - 使用property函数
    - property函数很简单
    - property(fget, fset, fdel, doc)

    ```python
    # 定义一个Person类，具有name，age属性
    # 对于任意输入的姓名，我们希望都用大写方式保存
    # 年龄，我们希望内部统一用整数保存
    # x = property(fget, fset, fdel, doc)
    class Person():
        '''
        这个是类的文档,
        在'print(Person.__doc__)'时显示.
        这是一个人，一个高尚的人，一个脱离了低级趣味的人
        他还他妈的有属性
        '''
        # 函数的名称可以任意
        # 读取操作
        def fget(self):
            return self._name * 2

        # 设定是操作
        def fset(self, name):
            # 所有输入的姓名以大写形式保存
            self._name = name.upper()

        # 删除时操作
        def fdel(self):
            self._name = "NoName"
        # 如果外部定义一个对象,那么先进行2→1→3
        name = property(fget, fset, fdel, "对name进行下下操作啦")

    p1 = Person()
    p1.name = "TuLing"
    print(p1.name)

    ```

    ```c
    TULINGTULING
    ```
- 无论哪种修饰符都是为了对成员属性进行相应的控制  
  - 类的方式： 适合多个类中的多个属性共用用一个描述符
  - property：使用当前类中使用，可以控制一个类中多个属性
  - 属性修饰符： 使用于当前类中使用，控制一个类中的一个属性
  
### 5.3 类的内置属性

        __dict__:以字典的方式显示类的成员组成
        __doc__: 获取类的文档信息
        __name__:获取类的名称，如果在模块中使用，获取模块的名称
        __bases__: 获取某个类的所有父类，以元组的方式显示

## 6. 类的常用魔术方法

- 魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发
- 魔术方法的统一的特征，方法名被前后各两个下滑线包裹
- 操作类
  - `__init__`: 构造函数
  - `__new__`: 对象实例化方法，此函数较特殊，一般不需要使用
  - `__call__`: 对象当函数使用的时候触发
  - `__str__`: 当对象被当做字符串使用的时候调用
  - `__repr__`: 返回字符串，跟`__str__`具体区别请百度
- 描述符相关
  - `__set__`
  - `__get__`
  - `__delete__`
- 属性操作相关
  - `__getattr__`: 访问一个不存在的属性时触发
  - `__setattr__`: 对成员属性进行设置的时候触发
    - 参数：
      - self用来获取当前对象
      - 被设置的属性名称，以字符串形式出现
      - 需要对属性名称设置的值
    - 作用：进行属性设置的时候进行验证或者修改
    - 注意： 在该方法中不能对属性直接进行赋值操作，否则死循环
    - 参看案例
- 运算分类相关魔术方法
  - `__gt__`: 进行大于判断(两个实例比较)的时候触发的函数
    - 参数：
      - self
      - 第二个参数是第二个对象
      - 返回值可以是任意值，推荐返回布尔值
      - 案例

### 类和对象的三种方法

- 实例方法
  - 需要实例化对象才能使用的方法，使用过程中可能需要截止对象的其他对象的方法完成
- 静态方法
  - 不需要实例化，通过类直接访问
- 类方法
  - 不需要实例化
- 案例
    ```python
    # 三种方法的案例
    class Person:
        # 实例方法
        def eat(self):
            print(self)
            print("Eating.....")

        #类方法
        # 类方法的第一个参数，一般命名为cls，区别于self
        @classmethod
        def play(cls):
            print(cls)
            print("Playing.....")

        # 静态方法
        # 不需要用第一个参数表示自身或者类
        @staticmethod
        def say():

            print("Saying....")

    yueyue = Person()

    # 实例方法
    yueyue.eat()
    # 类方法
    Person.play()
    yueyue.play()
    #静态方法
    Person.say()
    yueyue.say()
    ```

    ```c
    <__main__.Person object at 0x7f4aac6b3eb8>
    Eating.....
    <class '__main__.Person'>
    Playing.....
    <class '__main__.Person'>
    Playing.....
    Saying....
    Saying....
    ```

- 三个方法具体区别自行百度

| 是否自动传入第一个变量`self` | 实例方法 | 类方法 | 静态方法 |
| ---------------------------- | -------- | ------ | -------- |
| 类                           | 不会     | 会     | 不会     |
| 实例                         | 会       | 会     | 不会     |