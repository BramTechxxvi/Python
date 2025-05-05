class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.hour

    @hour.setter
    def hour(self, hour):
        if hour not in range(0, 24):
            raise ValueError(f'{hour} is invalid')
        self._hour = hour

    @property
    def minute(self):
        return self.minute

    @minute.setter
    def minute(self, minute):
        if minute not in range(0, 60):
            raise ValueError(f'{minute} is invalid')
        self._minute = minute

    @property
    def second(self):
        return self.second

    @second.setter
    def second(self, second):
        if second not in range(0, 60):
            raise ValueError(f'{second} is invalid')
        self._second = second

    def __str__(self):
        return f'{self.hour}:{self.minute}:{self.second}'

t2 = Time(23, 59, 59)
t2.hour(6)
t2.minute(20)
t2.second(8)
print(t2)


