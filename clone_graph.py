# coding=utf-8
# AC Rate: 22.7%
# SOURCE URL: https://oj.leetcode.com/problems/clone-graph/
#
#
# Clone an undirected graph. Each node in the graph contains a label and a
# list of its neighbors.
#
#
#
# OJ's undirected graph serialization:
#
# Nodes are labeled uniquely.
#
#
# We use # as a separator for each node, and , as a separator for node label
# and each neighbor of the node.
#
#
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
#
# The graph has a total of three nodes, and therefore contains three parts
# as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming
# a self-cycle.
#
#
#
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
#
#
import unittest


# Definition for a undirected graph node
class UndirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        if not node:
            return node
        # native
        nodes = {}
        stack = [node]
        while stack:
            n = stack.pop()
            if n.label in nodes:
                continue
            nodes[n.label] = UndirectedGraphNode(n.label)
            for neighbor in n.neighbors:
                # copy the label of the neighbors
                nodes[n.label].neighbors.append(neighbor.label)
                stack.append(neighbor)

        for n in nodes.values():
            for k, v in enumerate(n.neighbors):
                # transform labels to nodes
                n.neighbors[k] = nodes[v]
        return nodes[node.label]


class Test(unittest.TestCase):

    def setUp(self):
        from helper.graph import Graph
        self.g = Graph()
        self.s = Solution()
        self.g.load_leetcode_string('{0,1,2#1,2#2,2}')

    def test(self):
        cloneNode = self.s.cloneGraph(self.g.V['0'])
        self.assertEqual(cloneNode.label, '0')
        self.assertItemsEqual([n.label for n in cloneNode.neighbors],
                              ['1', '2'])


if __name__ == '__main__':
    unittest.main()
