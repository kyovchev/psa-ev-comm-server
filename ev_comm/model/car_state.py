from ev_comm.model.battery_state import BatteryState
from ev_comm.model.environment_state import EnvironmentState
from datetime import datetime


class CarState:
    def load_from_psacc_response(self, response):
        battery = BatteryState(
            response["energy"][0]["level"],
            response["energy"][0]["autonomy"],
            response["energy"][0]["charging"]["charging_mode"],
            response["energy"][0]["updated_at"]
        )

        environment = EnvironmentState(
            response["environment"]["air"]["temp"],
            response["environment"]["luminosity"]["day"]
        )

        self.battery = battery
        self.environment = environment
        self.odometer = response["timed_odometer"]["mileage"],
        self.ignition = response["ignition"]["type"]
        self.timestamp = datetime.timestamp(datetime.now())

    def to_dict(self):
        return {
            "battery": self.battery.to_dict(),
            "environment": self.environment.to_dict(),
            "odometer": self.odometer,
            "ignition": self.ignition,
            "timestamp": self.timestamp
        }
