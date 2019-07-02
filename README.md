# python_game



## Aircraft_Battle

1. [Aircraft_Battle]()

**飞机大战** 实战

## 模块使用pygame

* `pygame` 就是一个 Python 模块，专为电子游戏设计
* 官方网站：https://www.pygame.org/
    * **提示**：要学习第三方模块，通常最好的参考资料就在官方网站

| 网站栏目 | 内容 |
| --- | --- |
| `GettingStarted` | 在各平台安装模块的说明 |
| `Docs` | `pygame` 模块所有 **类** 和 **子类** 的参考手册 |

### 安装 pygame

```bash
$ sudo pip3 install pygame
```

### 验证安装

```bash
$ python3 -m pygame.examples.aliens
```

## 创建图形窗口

 1.游戏的初始化和推出

 2.游戏中的坐标系
 
 3.游戏主窗口
 

### 1.1 游戏的初始化和推出
 
* pygame.init()

* pygame.quit()

| 方法 | 说明 |
| --- | --- |
| `pygame.init()` | 导入并初始化所有 `pygame` 模块，使用其他模块之前，必须先调用 `init` 方法 |
| `pygame.quit()` | 卸载所有 `pygame` 模块，在游戏结束之前调用！ |


### 1.2 游戏中的坐标系

* **坐标系**
    * **原点** 在 **左上角** `(0, 0)`
    * **x 轴** 水平方向向 **右**，逐渐增加
    * **y 轴** 垂直方向向 **下**，逐渐增加

* pygame.Rect用于描述 **矩形区域**

```python
Rect(x, y, width, height) -> Rect
```

### 1.3 游戏主窗口

* pygame模块display用于创建、管理游戏窗口
| 方法 | 说明 |
| --- | --- |
| `pygame.display.set_model()` | 初始化窗口|
| `pygame.display.update()` | 刷新窗口 |



## 绘制游戏图像

1.使用pygame.image.load()加载

2.调用blit方法绘制到指定位置

3.调用display.update()方法更新

## 游戏的循环

> **游戏循环的开始** 就意味着 **游戏的正式开始**

1.设置刷新帧数

2.检查交互

3.更新图像的位置

4.更新显示

## 游戏时钟

* time.Clock 

* **tick**方法根据调用时间，自动设置游戏循环的时延 


## 游戏的监听

### 事件event
* 游戏的开始的时候，用户对游戏所作的操作

#### 监听
* 在游戏**循环**中 判断用户**操作**
 
    只有**捕获** 用户的才做，才能做出响应
* pygame中通过event.get()的方法获取**获取**用户动作


## 精灵与精灵族

* python.sprite.Sprite  存储图像数据和位置rect对象

* python.sprite.Group

## 游戏背景

* 背景滚动

1.创建两张相同背景图片

* 一张完全与屏幕重合
* 一张位于屏幕正上方

2.两张图片同时下移,交替滚动

## 定时器

### 利用定时器添加敌机
* set_timer(eventid, milliseconds)

1. 定义定时器常量

2. 初始化方法设置

3. 监听

## 敌机类

1. 游戏启动，每隔数秒出现敌机

2. 向屏幕下方飞行

3. 水平反向不一

## 飞机类

1. 游戏启动时，飞机出现在水平中间位置

2. 0.5发射子弹

3. 键盘模块控制飞机运动

### 子弹

1. 子弹从下往上飞

2. 子弹飞出屏幕，删除精灵族

### 键盘事件的捕获

* **第一种**

1. key_get_pressed() 返回所有按键元组

2. **键盘常量** 判断元组中是否按下

* **第二种**

1. **event.type**

## 碰撞检测

* groupcollide()

* spritecollide()

