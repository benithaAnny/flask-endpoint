import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_new_stack_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_push(self):
        stack = Stack()
        stack.push(10)

        self.assertEqual(stack.peek(), 10)
        self.assertEqual(stack.size(), 1)

    def test_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.size(), 1)

    def test_stack_is_lifo(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_peek_does_not_remove_item(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.size(), 2)

    def test_pop_empty_stack(self):
        stack = Stack()

        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_empty_stack(self):
        stack = Stack()

        with self.assertRaises(IndexError):
            stack.peek()


if __name__ == "__main__":
    unittest.main()