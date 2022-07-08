"""
@project:   dorado
@author:    ihc
@description:
"""


class _d_node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return '<{}({})>'.format(_d_node.__name__, str(self.val))

    def __repr__(self):
        return '<{}({})>'.format(_d_node.__name__, repr(self.val))


class _d_linked_list(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def add_first(self, e):
        """add the e to first node"""
        node = _d_node(e)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1

    def add_last(self, e):
        """add the e to last node"""
        node = _d_node(e)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        self._size += 1

    def get_last(self):
        return self._tail

    def get_first(self):
        return self._head

    def del_first(self):
        """del the first node, return the del node"""
        if not self._head:
            return None
        else:
            del_node = self._head
            print("1", self._head, self._head.next)
            self._head = self._head.next
            print("2", self._head, self._head.next)
            if self._head:
                self._head.prev = None
            self._size -= 1
            return del_node

    def del_last(self):
        """del the last node, return the del node"""
        if not self._tail:
            return None
        else:
            del_node = self._tail
            self._tail = self._tail.prev
            if self._tail:
                self._tail.next = None
            self._size -= 1
            return del_node

    def size(self):
        return self._size

    def val_to_list(self):
        current = self._head
        if not current:
            return None
        else:
            vals = []
            vals.append(current.val)
            while current.next:
                current = current.next
                vals.append(current.val)
            return vals


if __name__ == '__main__':
    d_li = _d_linked_list()

    d_li.add_first(1)
    d_li.add_first(2)
    d_li.add_first(3)
    # 3 2 1
    assert d_li.get_first().val == 3
    assert d_li.get_last().val == 1

    d_li.add_last(10)
    d_li.add_last(11)
    d_li.add_last(12)
    assert d_li.get_last().val == 12 and d_li.size() == 6
    assert d_li.get_last().prev.val == 11
    # 3 2 1 10 11 12

    d_li.del_first()
    assert d_li.get_first().val == 2 and d_li.size() == 5
    # 2 1 10 11 12

    d_li.del_last()
    assert d_li.get_last().val == 11 and d_li.size() == 4
    # 2 1 10 11

    d_li.del_last()
    d_li.del_last()
    d_li.del_last()
    # 2
    assert d_li.get_first().val == 2 and d_li.get_last().val == 2 and d_li.size() == 1

    d_li.del_first()

    print(d_li.get_last())
    print(d_li.get_first())
    assert d_li.get_first() is None and d_li.get_last() is None and d_li.size() == 0

    # d_li.del_first()
