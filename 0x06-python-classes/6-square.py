#!/usr/bin/python3
"""classes for singly-linked list."""


class Node:
    """a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set data of Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """a singly-linked list."""

    def __init__(self):
        """Initalize a SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert Node to SinglyLinkedList"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            head = self.__head
            while (head.next_node is not None and
                    head.next_node.data < value):
                head = head.next_node
            new.next_node = head.next_node
            head.next_node = new

    def __str__(self):
        """representation of a SinglyLinkedList."""
        values = []
        head = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            head = head.next_node
        return ('\n'.join(values))
