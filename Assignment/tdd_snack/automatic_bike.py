class AutomaticBike:

    def __init__(self):
        self.start_bike = False
        self.accelerate = 0
        self.currentGear = 0

    def switch_on_bike(self):
        if not self.start_bike:
            self.start_bike = True
            return True
        return False

    def switch_off_bike(self):
        self.start_bike = False
        self.accelerate = 0
        return False

    def set_gear(self, gear):
        if 1<= gear <=4:
            self.currentGear = gear

    def accelerate_bike(self):
        if self.start_bike:
            match self.currentGear:
                case 1:
                    if self.accelerate < 20: self.accelerate+=1
                case 2:
                    if self.accelerate < 30: self.accelerate+=2
                case 3:
                    if self.accelerate < 40: self.accelerate+=3
                case 4:
                    self.accelerate+=4
        return self.accelerate

    def decelerate_bike(self):
        if self.start_bike:
            match self.currentGear:
                case 1:
                    if self.accelerate < 20: self.accelerate -= 1
                case 2:
                    if self.accelerate < 30: self.accelerate -= 2
                case 3:
                    if self.accelerate > 0: self.accelerate -= 3
                case 4:
                    self.accelerate -= 4
        return self.accelerate

    def get_speed(self): return self.accelerate