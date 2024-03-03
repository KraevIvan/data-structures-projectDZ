"""Здесь надо написать тесты с использованием unittest для модуля stack_for_test."""
import unittest
from src.stack import Node, Stack

node_for_test1 = Node("data1")
node_for_test2 = Node("data2", node_for_test1)

stack_for_test = Stack()
stack_for_test.push('data1')
stack_for_test.push('data2')
stack_for_test.push('data3')


class TestNodeAndStack(unittest.TestCase):

    def test_Node(self):
        self.assertEqual(node_for_test1.data, "data1")
        self.assertEqual(node_for_test1.next_node, None)
        self.assertEqual(node_for_test2.next_node, node_for_test1)

    def test_Stack(self):
        self.assertEqual(stack_for_test.top.data, "data3")
        self.assertEqual(stack_for_test.top.next_node.data, "data2")
        self.assertEqual(stack_for_test.top.next_node.next_node.data, "data1")
        self.assertEqual(stack_for_test.top.next_node.next_node.next_node, None)

        self.assertEqual(stack_for_test.pop(),"data3")


if __name__ == '__main__':
    unittest.main()
