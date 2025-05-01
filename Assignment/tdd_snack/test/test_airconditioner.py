import unittest
from tdd_snack.airconditioner import AirConditioner
class TestAirConditioner(unittest.TestCase):

    def setUp(self):
        self.my_switch = AirConditioner()

    def test__init__(self):
        my_switch = AirConditioner()
        self.assertEqual(my_switch.is_on, False)

    def test_that_function_can_switch_ac_on(self):
        my_switch = AirConditioner()
        self.assertTrue(my_switch.switch_on_ac())

    def test_that_function_can_switch_ac_off(self):
        my_switch = AirConditioner()
        self.assertFalse(my_switch.switch_off_ac())

    def test_that_temperature_cannot_change_when_off(self):
        my_switch = AirConditioner()
        self.assertEqual(my_switch.increase_temperature(), 16)
        self.assertEqual(my_switch.decrease_temperature(), 16)

    def test_that_function_can_increase_temperature(self):
        my_switch = AirConditioner()
        self.assertTrue(my_switch.switch_on_ac())
        self.assertEqual(my_switch.increase_temperature(),17)
        for num in range(1, 21): my_switch.increase_temperature()
        self.assertEqual(my_switch.get_temperature(), 30)

    def test_that_function_can_decrease_temperature(self):
        my_switch = AirConditioner()
        self.assertTrue(my_switch.switch_on_ac())
        self.assertEqual(my_switch.increase_temperature() + 4, 21)
        for num in range(1, 10): my_switch.decrease_temperature()
        self.assertEqual(my_switch.get_temperature(), 16)

if __name__ == '__main__':
    unittest.main()