class BatteryState:
    def __init__(self, level, autonomy, charging_mode, updated_at):
        self.level = level
        self.autonomy = autonomy
        self.charging_mode = charging_mode
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "level": self.level,
            "autonomy": self.autonomy,
            "charging_mode": self.charging_mode,
            "updated_at": self.updated_at
        }
