class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubuleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None
    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count+=1
            cur = cur.next
        return count

if __name__ == '__main__':
    pass
