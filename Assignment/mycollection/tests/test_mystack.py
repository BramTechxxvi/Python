import unittest
from mycollection.mystack import MyStack
class TestMyStack(unittest.TestCase):

    def setUp(self):
        self.my_stack = MyStack(5)

    def test_if_stack_is_empty(self):
        my_stack = MyStack(3)
        self.assertTrue(my_stack.is_empty())

    def test_if_stack_is_full(self):
        my_stack = MyStack(3)
        my_stack.push(9)
        my_stack.push(10)
        my_stack.push(11)
        self.assertFalse(my_stack.is_empty())
        self.assertTrue(my_stack.is_full())


    def test_if_function_add_element_can_add(self):
        my_stack = MyStack(1)
        my_stack.push(4)
        my_stack.push(5)
        self.assertEqual(my_stack.data, [4, 5])
