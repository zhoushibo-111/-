class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        # 添加一个元素到栈顶
        self.__list.append(item)

    def pop(self):
        # 弹出栈顶的元素
        if self.__list:
            return self.__list.pop()
        else:
            return '空栈'
    def peek(self):
        '''返回栈顶元素'''
        if self.__list:
           return self.__list[-1]
        else:
            return None
    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    print(s.pop())
    print("--"*30)
    s.push(1)
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.peek())
    print(s.pop())
