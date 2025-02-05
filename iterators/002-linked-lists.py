# Завдання 2
# 
# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи:
#
# очищення списку
# додавання елемента у довільне місце списку, 
# видалення елемента з кінця 
# видалення елемента з довільного місця списку
#


class MyList(object):

    class _ListNode(object):
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        self._length = 0
        self._head = None
        self._tail = None

        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        node = MyList._ListNode(element)

        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1
    
    def insert(self, element, position: int):
        if position >= self._length:
            raise IndexError

        node = MyList._ListNode(element)

        if position == 0:
            node.next = self._head
            if self._head:
                self._head.prev = node
            self._head = node
            if self._tail is None:
                self._tail = node
        elif position == self._length -1:
            self.append(element)
        else:
            current = self._head
            for _ in range(position - 1):
                current = current.next
            node.next = current.next
            node.prev = current
            if current.next:
                current.next.prev = node
            current.next = node
    
        self._length += 1
    
    def pop(self):
        if self._tail is None:
            raise IndexError

        value = self._tail.value
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        
        self._length -= 1
        return value
    
    def delete(self, position):
        if position < 0 or position >= self._length:
            raise IndexError

        if position == 0:
            value = self._head.value
            self._head = self._head.next
            if self._head:
                self._head.prev = None
            else:
                self._tail = None
        elif position == self._length - 1:
            return self.pop()
        else:
            current = self._head
            for _ in range(position):
                current = current.next
            value = current.value
            current.prev.next = current.next
            current.next.prev = current.prev
        
        self._length -= 1
        return value
    
    def clear(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def __repr__(self):
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    my_list = MyList([1, 2, 5])
    print(my_list)

    # add element to any position
    my_list.insert(8, 2)
    my_list.insert(7, 0)
    print(my_list)

    my_list.pop()
    print(my_list)

    my_list.delete(0)
    print(my_list)




if __name__ == '__main__':
    main()
