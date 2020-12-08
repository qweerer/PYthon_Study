import numpy.random as np

class Turtle(object):
    def __init__ (self):
        self.heart = 100

        self.x = np.randint(0, 10)
        self.y = np.randint(0, 10)
    
    def move(self):
        move_x = np.choice([-2, -1, 0, 1, 2])
        move_all = np.choice([1, 2])
        move_dir = np.choice([-1, 1])
        move_y = move_dir * (move_all - abs(move_x))

        self.x = self.x + move_x
        self.y = self.y + move_y

        if self.x > 10:
            self.x = 20 - self.x
        elif self.x < 0:
            self.x = -self.x

        if self.y > 10:
            self.y = 20 - self.y
        elif self.y < 0:
            self.y = -self.y
        
        self.heart = self.heart - 1
    
    def eat(self, fish_list, fish_list_die):
        for fish_one in fish_list:
            if self.x == fish_one.x and self.y == fish_one.y:
                self.heart = self.heart + 20
                fish_list.remove(fish_one)
                fish_list_die.append(fish_one)
                fish_one.die()
                print('乌龟吃了{}'.format(fish_one.name))

class Fish(object):
    def __init__(self, name):
        self.name = name
        self.x = np.randint(0, 10)
        self.y = np.randint(0, 10)
        self.status = '存活'

    def move(self):
        move_x = np.choice([-2, -1, 0, 1, 2])
        move_y = np.choice([-1, 1]) * (np.choice([1, 2]) - abs(move_x))

        self.x = self.x + move_x
        self.y = self.y + move_y

        if self.x > 10:
            self.x = 20 - self.x
        elif self.x < 0:
            self.x = -self.x

        if self.y > 10:
            self.y = 20 - self.y
        elif self.y < 0:
            self.y = -self.y

    def die(self):
        self.status = '死亡'

# %% 初始化游戏
tur = Turtle()
fish_list = []
fish_list_die = []
for i in range(10):
    j = i+1
    exec('fish_{}=Fish("{}")'.format(j, '小鱼'+str(j)))
    exec('fish_list.append(fish_{})'.format(j))
    exec('del fish_{}'.format(j))
# %% 开始游戏

i = 0
while (tur.heart > 0) and (len(fish_list)>0):
    i = i+1
    print('本局游戏为第{}轮,情况是：'.format(i))

    tur.move()
    for j in fish_list:
        j.move()
    tur.eat(fish_list, fish_list_die)
    
    print('乌龟位置为：x={},y={}'.format(tur.x, tur.y))
    for j in fish_list:
        print('{}的状态是{}，位置是：x={},y={}'.format(j.name, j.status, j.x, j.y))
    for j in fish_list_die:
        print('{}的状态是{}，位置是：x={},y={}'.format(j.name, j.status, j.x, j.y))
    
    print('*'*10)

print('#'*20)
print('游戏结束')
if tur.heart > 0:
    print('乌龟获胜')
else:
    print('鱼获胜')