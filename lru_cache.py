# coding=utf-8
# AC Rate: 13.9%
# SOURCE URL: https://oj.leetcode.com/problems/lru-cache/
#
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
#
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
#
import unittest

class LRUCache:

    class DoubleLinkListNode():
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    class DoubleLinkList():
        def __init__(self):
            self.head = None
            self.tail = None

        def add_tail(self, node):
            if not self.tail:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node

        def move_to_tail(self, node):
            if not node.next:
                # tail
                return
            if not node.prev:
                # head
                self.head = node.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            node.prev = None
            node.next = None
            self.add_tail(node)

        def remove_head(self):
            if self.head == self.tail:
                # only happen when capacity == 1
                self.head = None
                self.tail = None
                return
            self.head = self.head.next
            self.head.prev = None

        def render(self):
            res = []
            node = self.head
            while node:
                res.append(node.key)
                node = node.next
            return res

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.lru = self.DoubleLinkList()

    # @return an integer
    def get(self, key):
        if key not in self.dic:
            return -1
        else:
            self.lru.move_to_tail(self.dic[key])
            return self.dic[key].val


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.dic:
            if len(self.dic.keys()) >= self.capacity:
                del self.dic[self.lru.head.key]
                self.lru.remove_head()
            self.dic[key] = self.DoubleLinkListNode(key, value)
            self.lru.add_tail(self.dic[key])
        else:
            self.dic[key].val = value
            self.lru.move_to_tail(self.dic[key])


class Test(unittest.TestCase):
    def test1(self):
        l = LRUCache(3)
        l.set(0, 0)
        self.assertEqual(l.get(0), 0)
        l.set(1, 1)
        l.set(2, 2)
        l.set(3, 3)
        self.assertEqual(l.get(0), -1)
        self.assertEqual(l.get(3), 3)
        self.assertEqual(l.get(2), 2)
        self.assertEqual(l.get(1), 1)
        l.set(4, 4)
        self.assertEqual(l.get(3), -1)

    def test2(self):
        l = LRUCache(1)
        l.set(2,1)
        self.assertEqual(l.get(2), 1)
        l.set(3,2)
        self.assertEqual(l.get(2), -1)
        self.assertEqual(l.get(3), 2)

    def test3(self):
        l = LRUCache(10)
        l.set(10,13)
        l.set(3,17)
        l.set(6,11)
        l.set(10,5)
        l.set(9,10)
        self.assertEqual(l.get(13), -1)
        l.set(2,19)
        self.assertEqual(l.lru.render(), [3, 6, 10, 9, 2])
        self.assertEqual(l.get(2), 19)
        self.assertEqual(l.lru.render(), [3, 6, 10, 9, 2])
        self.assertEqual(l.get(3), 17)
        self.assertEqual(l.lru.render(), [6, 10, 9, 2, 3])
        l.set(5,25)
        self.assertEqual(l.get(8), -1)
        l.set(9,22)
        l.set(5,5)
        l.set(1,30)
        l.get(11)
        l.set(9,12)
        l.get(7)
        l.get(5)
        l.get(8)
        l.get(9)
        l.set(4,30)
        l.set(9,3)
        l.get(9)
        l.get(10)
        l.get(10)
        l.set(6,14)
        l.set(3,1)
        l.get(3)
        l.set(10,11)
        l.get(8)
        l.set(2,14)
        l.get(1)
        l.get(5)
        l.get(4)
        l.set(11,4)
        l.set(12,24)
        l.set(5,18)
        l.get(13)
        l.set(7,23)
        l.get(8)
        l.get(12)
        l.set(3,27)
        l.set(2,12)
        l.get(5)
        l.set(2,9)
        l.set(13,4)
        l.set(8,18)
        l.set(1,7)
        self.assertEqual(l.get(6), -1)
        l.set(9,29)
        l.set(8,21)
        self.assertEqual(l.get(5), 18)
        l.set(6,30)
        l.set(1,12)
        l.get(10)
        l.set(4,15)
        l.set(7,22)
        l.set(11,26)
        l.set(8,17)
        l.set(9,29)
        l.get(5)
        l.set(3,4)
        l.set(11,30)
        l.get(12)
        l.set(4,29)
        l.get(3)
        l.get(9)
        l.get(6)
        l.set(3,4)
        l.get(1)
        l.get(10)
        l.set(3,29)
        l.set(10,28)
        l.set(1,20)
        l.set(11,13)
        l.get(3)
        l.set(3,12)
        l.set(3,8)
        l.set(10,9)
        l.set(3,26)
        l.get(8)
        l.get(7)
        l.get(5)
        l.set(13,17)
        l.set(2,27)
        l.set(11,15)
        l.get(12)
        l.set(9,19)
        l.set(2,15)
        l.set(3,16)
        l.get(1)
        l.set(12,17)
        l.set(9,1)
        l.set(6,19)
        l.get(4)
        l.get(5)
        l.get(5)
        l.set(8,1)
        l.set(11,7)
        l.set(5,2)
        l.set(9,28)
        l.get(1)
        l.set(2,2)
        l.set(7,4)
        l.set(4,22)
        l.set(7,24)
        l.set(9,26)
        l.set(13,28)
        l.set(11,26)



if __name__ == '__main__':
    unittest.main()
