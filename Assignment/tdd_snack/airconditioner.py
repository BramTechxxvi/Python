class AirConditioner:

    def __init__(self):
        self.is_on = False
        self.temperature = 16

    def switch_on_ac(self):
        if not self.is_on:
            self.is_on = True
            return True
        return False

    def switch_off_ac(self):
        self.is_on = False
        self.temperature = 0
        return False

    def increase_temperature(self):
        if self.is_on is True:
            self.temperature += 1
            if self.temperature >= 30:
                self.temperature = 30
        return self.temperature

    def decrease_temperature(self):
        if self.is_on is True:
            self.temperature -= 1
            if self.temperature <= 16:
                self.temperature = 16
        return self.temperature

    def get_temperature(self):
        return self.temperature

