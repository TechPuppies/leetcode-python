# coding=utf-8
import unittest


class TreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree():

    def __init__(self):
        self.head = None

    def load_array(self, array):
        if not array:
            return None
        head = TreeNode(array.pop(0))
        queue = [head]
        while array:
            node = queue.pop(0)
            l = array.pop(0) if array else None
            if l is not None:
                node.left = TreeNode(l)
                queue.append(node.left)
            r = array.pop(0) if array else None
            if r is not None:
                node.right = TreeNode(r)
                queue.append(node.right)
        self.head = head

    def load_leetcode_string(self, lc_str):
        lc_str = lc_str[1:-1]
        array = lc_str.split(',')
        for i in range(len(array)):
            array[i] = None if array[i] == '#' else int(array[i])
        return self.load_array(array)


class Test(unittest.TestCase):

    def test(self):

        t = Tree()
        t.load_array([1, 2, 3, None, 4])
        self.assertEqual(t.head.val, 1)
        self.assertEqual(t.head.left.val, 2)
        self.assertEqual(t.head.right.val, 3)
        self.assertEqual(t.head.left.left, None)
        self.assertEqual(t.head.left.right.val, 4)

    def test2(self):
        t = Tree()
        t.load_leetcode_string('{1,2,3,#,4}')
        self.assertEqual(t.head.val, 1)
        self.assertEqual(t.head.left.val, 2)
        self.assertEqual(t.head.right.val, 3)
        self.assertEqual(t.head.left.left, None)
        self.assertEqual(t.head.left.right.val, 4)

    def test3(self):
        t = Tree()
        t.load_leetcode_string('{1,#,2,3}')
        self.assertEqual(t.head.val, 1)
        self.assertEqual(t.head.right.val, 2)
        self.assertEqual(t.head.right.left.val, 3)

if __name__ == '__main__':
    unittest.main()
