import unittest
from linked_lists.circular import CircularLinkedList

class TestCircularLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = CircularLinkedList()
        for char in "ABCDE":
            self.list.append(char)

    def test_length(self):
        self.assertEqual(self.list.length(), 5)

    def test_append_and_get(self):
        self.list.append('F')
        self.assertEqual(self.list.get(5), 'F')

    def test_insert(self):
        self.list.insert('Z', 2)
        self.assertEqual(self.list.get(2), 'Z')
        self.assertEqual(self.list.length(), 6)
        with self.assertRaises(IndexError):
            self.list.insert('Q', 100)

    def test_delete(self):
        removed = self.list.delete(1)
        self.assertEqual(removed, 'B')
        self.assertEqual(self.list.length(), 4)
        with self.assertRaises(IndexError):
            self.list.delete(10)

    def test_deleteAll(self):
        self.list.append('A')
        self.list.deleteAll('A')
        self.assertEqual(self.list.findFirst('A'), -1)

    def test_clone(self):
        clone = self.list.clone()
        self.assertEqual(clone.length(), self.list.length())
        clone.delete(0)
        self.assertNotEqual(clone.length(), self.list.length())

    def test_reverse(self):
        orig = [self.list.get(i) for i in range(self.list.length())]
        self.list.reverse()
        rev = [self.list.get(i) for i in range(self.list.length())]
        self.assertEqual(rev, orig[::-1])
        self.assertEqual(self.list.get(0), orig[-1])

    def test_find(self):
        self.assertEqual(self.list.findFirst('C'), 2)
        self.assertEqual(self.list.findLast('C'), 2)
        self.assertEqual(self.list.findFirst('X'), -1)

    def test_clear(self):
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_extend(self):
        other = CircularLinkedList()
        other.append('X')
        other.append('Y')
        self.list.extend(other)
        self.assertEqual(self.list.length(), 7)
        self.assertEqual(self.list.get(5), 'X')
        self.assertEqual(self.list.get(6), 'Y')

if __name__ == '__main__':
    unittest.main()
