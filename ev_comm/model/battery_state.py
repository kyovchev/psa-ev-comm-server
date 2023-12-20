class BatteryState:
    def __init__(self, level, autonomy, charging, updated_at):
        self.level = level
        self.autonomy = autonomy
        self.charging = charging
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "level": self.level,
            "autonomy": self.autonomy,
            "charging": self.charging.to_dict(),
            "updated_at": self.updated_at
        }
