class ArrayBasedList:
    def __init__(self):
        self.items = []

    def append(self, element: str) -> None:
        self.items.append(element)

    def length(self) -> int:
        return len(self.items)

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.length():
            raise ValueError("Wrong index value.")
        self.items.insert(index, element)

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise ValueError("Wrong index value.")
        return self.items.pop(index)

    def get(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise ValueError("Wrong index value.")
        return self.items[index]

    def deleteAll(self, element: str) -> None:
        self.items = [item for item in self.items if item != element]

    def clone(self) -> 'ArrayBasedList':
        cloned = ArrayBasedList()
        cloned.items = self.items.copy()
        return cloned

    def reverse(self) -> None:
        self.items.reverse()

    def findFirst(self, element: str) -> int:
        try:
            return self.items.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str) -> int:
        for i in range(self.length() - 1, -1, -1):
            if self.items[i] == element:
                return i
        return -1

    def clear(self) -> None:
        self.items = []

    def extend(self, other: 'ArrayBasedList') -> None:
        self.items.extend(other.items.copy())
