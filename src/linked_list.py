class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None:
            self.head = Node(data, self.tail)
            self.tail = self.head
        else:
            new_node = Node(data, None)
            self.tail.next_node = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ""
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node

        ll_string += "None"
        return ll_string

    def to_list(self):
        node = self.head
        list_all = []
        while node is not None:
            list_all.append(node.data)
            node = node.next_node
        return list_all

    def get_data_by_id(self, id_):
        list_ = self.to_list()
        for item in list_:
            try:
                if item['id'] == id_:
                    return item
            except TypeError:
                continue
        return f"Данные не являются словарем или в словаре нет id."
