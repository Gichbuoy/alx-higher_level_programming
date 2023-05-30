#!/bin/usr/python3
"""Define classes for a linked list"""


class Node:
    """creates a class calles node """

    def __init__(self, value, next_node=None):
        """Initialize variables"""
        self.value = value
        self.next_node = next_node

    @property
    def value(self):
        """define the values of the Node."""
        return self.__value

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise TypeError("value must be an integer")
        self.__value = val

    @property
    def next_node(self):
        """define the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        if not isinstance(node, Node) and node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = node


class SinglyLinkedList:
    """creates a class """

    def __init__(self):
        """Initialize a new LinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """define variables"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.value > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                    current_node.next_node.value < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """Define of variables of linkedlistt."""
        values = []
        current_node = self.__head
        while current_node is not None:
            values.append(str(current_node.value))
            current_node = current_node.next_node
        return '\n'.join(values)
