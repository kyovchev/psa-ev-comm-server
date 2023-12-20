class PositionState:
    def __init__(self, longitude, latitude,  altitude, updated_at):
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "longitude": self.longitude,
            "latitude": self.latitude,
            "altitude": self.altitude,
            "updated_at": self.updated_at
        }
