class ChargingState:
    def __init__(self, mode, rate, plugged, remaining_time, status):
        self.mode = mode
        self.rate = rate
        self.plugged = plugged
        self.remaining_time = remaining_time
        self.status = status

    def to_dict(self):
        return {
            "mode": self.mode,
            "rate": self.rate,
            "plugged": self.plugged,
            "remaining_time": self.remaining_time,
            "status": self.status
        }
