class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, element: str) -> None:
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def length(self) -> int:
        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.length():
            raise ValueError("Wrong index value.")

        new_node = Node(element)
        if index == 0:
            if not self.head:
                self.head = new_node
                new_node.next = new_node
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                new_node.next = self.head
                self.head = new_node
                current.next = self.head
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def get(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise ValueError("Wrong index value.")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise ValueError("Wrong index value.")

        if self.length() == 1:
            data = self.head.data
            self.head = None
            return data

        if index == 0:
            current = self.head
            while current.next != self.head:
                current = current.next
            data = self.head.data
            self.head = self.head.next
            current.next = self.head
            return data
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            data = prev.next.data
            prev.next = prev.next.next
            return data


if __name__ == '__main__':
    clist = CircularLinkedList()
    print("Initial length (expected 0):", clist.length())
    clist.append('A')
    clist.append('B')
    clist.append('C')
    print("Length after appending A, B, C (expected 3):", clist.length())
    clist.insert('D', 0)
    print("Element at index 0 after insert (expected D):", clist.get(0))
    clist.insert('E', 2)
    print("Element at index 2 after insert (expected E):", clist.get(2))
    deleted = clist.delete(1)
    print("Deleted element at index 1 (expected A):", deleted)
    print("Length after deletion:", clist.length())
