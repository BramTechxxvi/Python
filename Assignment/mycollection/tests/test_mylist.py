import unittest
from mycollection.mylist import MyList
class TestMyList(unittest.TestCase):

    def setUp(self):
        self.my_method = MyList()

    def test__init__(self):
        my_method = MyList()
        self.assertEqual(my_method.items, [])

    def test_if_function_add_element_can_add(self):
        my_method = MyList()
        my_method.add_element(5)
        self.assertEqual(my_method.items, [5])
        my_method.add_element(17)
        my_method.add_element("Anikulapo")
        my_method.add_element(-190)
        my_method.add_element(18.87)
        self.assertEqual(my_method.items, [5,17,"Anikulapo",-190,18.87])

    def test_function_remove_element_can_delete(self):
        my_method = MyList()
        my_method.remove_element(5)
        self.assertEqual(my_method.items, [])
        my_method.add_element(1)
        my_method.remove_element(1)
        self.assertEqual(my_method.items, [])
        my_method.add_element(1)
        my_method.add_element(-17)
        my_method.add_element("Intercept")
        my_method.add_element(10.67)
        my_method.add_element("Blockchain")
        my_method.remove_element(-17)
        my_method.remove_element("Blockchain")
        user_input = my_method.remove_element("Coke")
        self.assertIsNone(user_input)
        self.assertEqual(my_method.items, [1, "Intercept", 10.67])

    def test_if_function_extend_element_can_add_element_into_list(self):
        my_method = MyList()
        military = ["Navy", "Police", "Army"]
        my_method.extend_element(military)
        self.assertEqual(my_method.items, ["Navy", "Police", "Army"])
        paramilitary = ["Civil defense", "Legion", "Boys scout"]
        my_method.extend_element(paramilitary)
        self.assertEqual(my_method.items, ["Navy", "Police", "Army", "Civil defense", "Legion", "Boys scout"])

    def test_if_function_clear_can_delete_all_element_in_list(self):
        my_method = MyList()
        my_method.add_element("Book")
        my_method.clear_element()
        self.assertEqual(my_method.items, [] )
        vegetables = ["Okra", "lettuce", "onion", "Tomato", "pepper"]
        my_method.extend_element(vegetables)
        my_method.clear_element()
        self.assertEqual(my_method.items, [])

    def test_if_count_function_can_get_number_of_elements_in_list(self):
        my_method = MyList()
        first_count = my_method.count_element(my_method.items)
        self.assertEqual(first_count, 0)
        user_input1 = [90, "tomato", "pepper", "onion", "#"]
        my_method.extend_element(user_input1)
        my_method.add_element(299)
        my_method.add_element("%")
        user_input2 = ["%", 23.90, "Kehinde", -7, 299, "Onion"]
        my_method.extend_element(user_input2)
        second_count = my_method.count_element("Onion")
        self.assertEqual(second_count, 1)

    def test_if_function_can_copy_elements_in_list(self):
        my_method = MyList()
        my_method.add_element(5)
        gadgets = ["Laptop","Headphone","Soundbox"]
        my_method.extend_element(gadgets)
        my_method.add_element(17)
        self.assertEqual(my_method.items, [5,"Laptop","Headphone", "Soundbox",17])
        self.assertIsNot([], my_method.items)

    def test_if_function_can_get_index_of_element(self):
        my_method = MyList()
        my_method.add_element(5)
        my_method.add_element("Headphone")
        my_method.add_element("Phone")
        my_method.add_element(-18.9)
        pick_list = ["Soundbox", '#', "Horse", 14, "letter", 1000]
        my_method.extend_element(pick_list)
        self.assertEqual(my_method.get_index_of_element("Soundbox"), 4)
        self.assertEqual(my_method.get_index_of_element(1000), 9)
        self.assertEqual(my_method.get_index_of_element("Headphone"), 1)
        self.assertEqual(my_method.get_index_of_element(7), None)
        result = my_method.get_index_of_element(10)
        self.assertIsNone(result)

    def test_if_function_can_insert_elements_into_list(self):
        my_method = MyList()
        my_method.add_element("Garri")
        my_method.add_element("Headphone")
        my_method.add_element("Suya")
        my_method.insert_element(0,"Water")
        self.assertEqual(my_method.items, ["Water", "Garri", "Headphone", "Suya"])
        my_method.insert_element(11,"you")
        self.assertEqual(my_method.items, ["Water", "Garri", "Headphone", "Suya", "you"])

    def test_if_function_can_sort_elements_in_list(self):
        my_method = MyList()
        my_method.add_element("Stark")
        user_input = ["Bak", "Greece","Jackpot"]
        my_method.extend_element(user_input)
        my_method.sort_element()
        self.assertEqual(my_method.items, ["Bak", "Greece", "Jackpot", "Stark"])

if __name__ == '__main__':
    unittest.main()