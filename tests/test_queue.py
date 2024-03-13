"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue

node_for_test1 = Node("data1n")
node_for_test2 = Node("data2n", node_for_test1)

queue_for_test = Queue()
queue_for_test.enqueue('data1')
queue_for_test.enqueue('data2')
queue_for_test.enqueue('data3')


class TestNodeAndStack(unittest.TestCase):

    def test_Node(self):
        self.assertEqual(node_for_test1.data, "data1n")
        self.assertEqual(node_for_test1.next_node, None)
        self.assertEqual(node_for_test2.next_node, node_for_test1)

    def test_Queue(self):
        self.assertEqual(queue_for_test.head.data, "data1")
        self.assertEqual(queue_for_test.tail.data, "data3")
        self.assertEqual(queue_for_test.dequeue(), "data1")
        self.assertEqual(queue_for_test.dequeue(), "data2")
        self.assertEqual(queue_for_test.dequeue(), "data3")
        self.assertEqual(queue_for_test.dequeue(), None)

    def test_Queue_str(self):
        self.assertEqual(str(queue_for_test), "data1\ndata2\ndata3")


if __name__ == '__main__':
    unittest.main()