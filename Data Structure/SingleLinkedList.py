class Node:
    """링크드 리스트의 노드"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """링크드리스트 클래스"""

    def __init__(self):
        self.head = None
        self.tail = None

    def pop_left(self):
        """링크드 리스트 맨 앞 노드 제거; 링크드 리스트에 항상 노드가 있다는 가정 하에"""
        head = self.head

        if head == self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next

        return head.data

    def preprend(self, data):
        """링크드 리스트 맨 앞에 노드 추가"""
        new_node = Node(data)

        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head

        self.head = new_node

    def __str__(self):
        string = ""

        iterator = self.head

        while iterator is not None:
            string += f"{iterator.data} |"
            iterator = iterator.next

        return string
