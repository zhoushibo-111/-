class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        '''往队列添加一个元素'''
        '''选择从头部添加还是从尾部添加，看是多数操作是出队还是入队'''
        self.__list.append(item)
        #self.__list.insert(0, item)

    def dequeue(self):
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
    s = Queue()
    print(s.dequeue())
    print("--"*30)
    s.enqueue(1)
    s.enqueue(1)
    s.enqueue(2)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())