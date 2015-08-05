class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)
