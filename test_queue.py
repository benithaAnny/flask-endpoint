import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_new_queue_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(10)

        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.size(), 1)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)

        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.size(), 1)

    def test_queue_is_fifo(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)

    def test_peek_does_not_remove_item(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)

        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.size(), 2)

    def test_dequeue_empty_queue(self):
        queue = Queue()

        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_peek_empty_queue(self):
        queue = Queue()

        with self.assertRaises(IndexError):
            queue.peek()


if __name__ == "__main__":
    unittest.main()