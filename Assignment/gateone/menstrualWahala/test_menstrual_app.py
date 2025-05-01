import unittest
from gateone.menstrualWahala.menstrual_app import MenstrualApp
class TestMenstrualApp(unittest.TestCase):

    def setUp(self):
        self.my_tracker = MenstrualApp()

    def test_if_function_can_get_flow_perioda(self):
        my_tracker = MenstrualApp()
        self.assertEqual(my_tracker.get_flow_period, 0)


if __name__ == '__main__':
    unittest.main()