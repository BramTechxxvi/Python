class AutomaticBike:

    def __init__(self):
        self.start_bike = False
        self.accelerate = 0

    def switch_on_bike(self):
        if not self.start_bike:
            self.start_bike = True
            return True
        return False

    def switch_off_bike(self):
        pass
