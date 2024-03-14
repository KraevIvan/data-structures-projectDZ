"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import LinkedList, Node
import unittest

node_for_test1 = Node("data1n")
node_for_test2 = Node("data2n", node_for_test1)

ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})


class TestNodeAndLinkedList(unittest.TestCase):

    def test_Node(self):
        self.assertEqual(node_for_test1.data, "data1n")
        self.assertEqual(node_for_test1.next_node, None)
        self.assertEqual(node_for_test2.next_node, node_for_test1)

    def test_Linked_list(self):
        assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


if __name__ == '__main__':
    unittest.main()