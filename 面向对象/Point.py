class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")


class Parent:  # 定义父类
    parentAttr = 100
    __par = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent, Point):
    def __init__(self):
        print("子类的构造方法")
    def parentMethod(self):
        print('调用子类方法 %d')

c = Child()
print(c.parentAttr)
#print(c.__par)
c.parentMethod()
c.setAttr(200)
del c
