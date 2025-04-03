import unittest
from linked_lists.array_based import ArrayBasedList

class TestArrayBasedList(unittest.TestCase):
    def setUp(self):
        self.list = ArrayBasedList()
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
        with self.assertRaises(ValueError):
            self.list.insert('Q', 100)

    def test_delete(self):
        removed = self.list.delete(1)
        self.assertEqual(removed, 'B')
        self.assertEqual(self.list.length(), 4)
        with self.assertRaises(ValueError):
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


if __name__ == '__main__':
    unittest.main()
