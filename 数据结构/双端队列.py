class SDeque(object):
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        '''往队列添加一个元素'''
        self.__list.insert(0,item)

    def add_rear(self, item):
        '''往队列添加一个元素'''
        '''选择从头部添加还是从尾部添加，看是多数操作是出队还是入队'''
        self.__list.append(item)
    def pop_front(self):
        '''从队列头删除一个元素'''
        if self.__list:
            return self.__list.pop(0)
        else:
            return '空队列'
    def pop_rear(self):
        '''从队列头删除一个元素'''
        if self.__list:
            return self.__list.pop()
        else:
            return '空队列'
    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    s = SDeque()

    print("--" * 30)
    s.add_front(1)
    s.add_front(1)
    s.add_rear(2)
    print(s.pop_rear())
    print(s.pop_rear())
    print(s.pop_rear())