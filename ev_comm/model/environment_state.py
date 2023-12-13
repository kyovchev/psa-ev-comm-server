class EnvironmentState:
    def __init__(self, air_temp, day):
        self.air_temp = air_temp
        self.day = day

    def to_dict(self):
        return {
            "air_temp": self.air_temp,
            "day": self.day
        }
