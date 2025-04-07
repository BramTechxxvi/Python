import unittest
from tdd_snack.automatic_bike import AutomaticBike
class AutomaticBikeTest(unittest.TestCase):

    def setUp(self):
        self.bike_control = ()

    def test__init__(self):
        bike_control = AutomaticBike()
        self.assertTrue(bike_control.start_bike, False)

    def test_that_function_can_switch_on_bike(self):
        assertFalse(sw)
