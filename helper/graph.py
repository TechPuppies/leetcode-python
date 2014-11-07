import unittest


class UndirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Graph:

    def __init__(self):
        self.V = {}
        self.E = {}

    def load_matrix(self, matrix):
        for row in matrix:
            self.V[row[0]] = UndirectedGraphNode(row[0])

        for row in matrix:
            for i in row[1:]:
                self.V[row[0]].neighbors.append(self.V[i])

        return self

    def load_leetcode_string(self, lc_str):
        lc_str = lc_str[1:-1]
        matrix = lc_str.split('#')
        for i in range(len(matrix)):
            matrix[i] = matrix[i].split(',')
        return self.load_matrix(matrix)


class Test(unittest.TestCase):

    def setUp(self):
        self.g = Graph()

    def test(self):
        self.g.load_matrix([[0, 1, 2], [1, 2], [2, 2]])
        self.assertItemsEqual(self.g.V.keys(), [0, 1, 2])
        self.assertItemsEqual(self.g.V[0].neighbors,
                          [self.g.V[1], self.g.V[2]])
        self.assertItemsEqual(self.g.V[1].neighbors,
                          [self.g.V[2]])
        self.assertItemsEqual(self.g.V[2].neighbors,
                          [self.g.V[2]])

    def test2(self):
        self.g.load_leetcode_string('{0,1,2#1,2#2,2}')
        self.assertItemsEqual(self.g.V.keys(), ['0', '1', '2'])
        self.assertItemsEqual(self.g.V['0'].neighbors,
                          [self.g.V['1'], self.g.V['2']])
        self.assertItemsEqual(self.g.V['1'].neighbors,
                          [self.g.V['2']])
        self.assertItemsEqual(self.g.V['2'].neighbors,
                          [self.g.V['2']])


if __name__ == '__main__':
    unittest.main()

