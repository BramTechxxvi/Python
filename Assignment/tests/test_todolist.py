import unittest
import todolist

class TestToDoListApp(unittest.TestCase):

    def test_that_add_task_function_exist(self):
        input1 = "SK"
        todolist.get_add_task(input1)

    def test_that_add_task_function_return_invalid(self):
        input2 = '90'
        actual = todolist.get_add_task(input2)
        result = "Invalid input... Enter task again" 
        self.assertEqual(actual, result)

    #def test 



if __name__ == "__main__":
    unittest.main()