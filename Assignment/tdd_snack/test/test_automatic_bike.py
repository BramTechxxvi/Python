import unittest
from tdd_snack.automatic_bike import AutomaticBike
class AutomaticBikeTest(unittest.TestCase):

    def setUp(self):
        self.bike_control = AutomaticBike()

    def test__init__(self):
        bike_control = AutomaticBike()
        self.assertEqual(bike_control.start_bike, False)
        self.assertEqual(bike_control.accelerate, 0)

    def test_that_function_can_switch_on_bike(self):
        bike_control = AutomaticBike()
        self.assertTrue(bike_control.switch_on_bike())

    def test_that_function_can_switch_off_bike(self):
        bike_control = AutomaticBike()
        self.assertFalse(bike_control.switch_off_bike())

    def test_that_automatic_bike_cannot_accelerate_when_off(self):
        bike_control = AutomaticBike()
        self.assertEqual(bike_control.accelerate_bike(), 0)

    def test_that_automatic_bike_can_accelerate_in_gear_one(self):
        bike_control = AutomaticBike()
        bike_control.switch_on_bike()
        bike_control.set_gear(1)
        bike_control.accelerate_bike()
        self.assertEqual(bike_control.get_speed(), 1)

    def test_that_automatic_bike_can_accelerate_in_gear_two(self):
        bike_control = AutomaticBike()
        bike_control.switch_on_bike()
        bike_control.set_gear(2)
        bike_control.accelerate_bike()
        self.assertEqual(bike_control.get_speed(), 2)

    def test_that_automatic_bike_can_accelerate_in_gear_three(self):
        bike_control = AutomaticBike()
        bike_control.switch_on_bike()
        bike_control.set_gear(3)
        bike_control.accelerate_bike()
        self.assertEqual(bike_control.get_speed(), 3)

    def test_that_automatic_bike_can_accelerate_in_gear_four(self):
        bike_control = AutomaticBike()
        bike_control.switch_on_bike()
        bike_control.set_gear(4)
        bike_control.accelerate_bike()
        self.assertEqual(bike_control.get_speed(), 4)

    def test_that_automatic_bike_can_decelerate_in_gear_one(self):
        bike_control = AutomaticBike()
        bike_control.switch_on_bike()
        bike_control.set_gear(1)
        for num in range(1, 6): bike_control.accelerate_bike()
        bike_control.decelerate_bike()
        self.assertEqual(bike_control.get_speed(), 4)

    def test_that_automatic_bike_can_decelerate_in_gear_two(self):
        bike_control = AutomaticBike()
        bike_control.switch_on_bike()
        bike_control.set_gear(2)
        for num in range(1, 6): bike_control.accelerate_bike()
        bike_control.decelerate_bike()
        bike_control.decelerate_bike()
        self.assertEqual(bike_control.get_speed(), 6)

    def test_that_automatic_bike_can_decelerate_in_gear_three(self):
        bike_control = AutomaticBike()
        bike_control.switch_on_bike()
        bike_control.set_gear(3)
        for num in range(3): bike_control.accelerate_bike()
        bike_control.decelerate_bike()
        self.assertEqual(bike_control.get_speed(), 6)

    def test_that_automatic_bike_can_decelerate_in_gear_four(self):
        bike_control = AutomaticBike()
        bike_control.switch_on_bike()
        bike_control.set_gear(4)
        for num in range(11): bike_control.accelerate_bike()
        bike_control.decelerate_bike()
        self.assertEqual(bike_control.get_speed(), 40)