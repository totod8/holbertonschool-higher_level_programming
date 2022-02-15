#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            new_node.next_node = tmp.next_node
            while tmp.next_node and value > tmp.next_node.data:
                new_node.next_node = tmp.next_node.next_node
                tmp = tmp.next_node
            tmp.next_node = new_node

    def __init__(self):
        self.__head = None

    def __str__(self):
        __list = ""
        current_node = self.__head
        while current_node:
            __list += str(current_node.data) + "\n"
            current_node = current_node.next_node
        __list = __list[:-1]
        return __list
