class SDeque(object):
    def __init__(self):
        self.__list = []

    def add_front(self, item):

        self.__list.insert(0,item)

    def add_rear(self, item):

        self.__list.append(item)
    def pop_front(self):

        if self.__list:
            return self.__list.pop(0)
        else:
            return '空队列'
    def pop_rear(self):

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