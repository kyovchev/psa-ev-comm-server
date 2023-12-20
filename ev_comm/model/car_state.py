from ev_comm.model.battery_state import BatteryState
from ev_comm.model.charging_state import ChargingState
from ev_comm.model.environment_state import EnvironmentState
from ev_comm.model.position_state import PositionState
from datetime import datetime


class CarState:
    def load_from_psacc_response(self, response):
        self.battery = BatteryState(
            response["energy"][0]["level"],
            response["energy"][0]["autonomy"],
            ChargingState(
                response["energy"][0]["charging"]["charging_mode"],
                response["energy"][0]["charging"]["charging_rate"],
                response["energy"][0]["charging"]["plugged"],
                response["energy"][0]["charging"]["remaining_time"],
                response["energy"][0]["charging"]["status"],
            ),
            response["energy"][0]["updated_at"]
        )

        self.environment = EnvironmentState(
            response["environment"]["air"]["temp"],
            response["environment"]["luminosity"]["day"]
        )

        self.position_state = PositionState(
            response["last_position"]["geometry"]["coordinates"][0],
            response["last_position"]["geometry"]["coordinates"][1],
            response["last_position"]["geometry"]["coordinates"][2],
            response["last_position"]["properties"]["updated_at"]
        )

        self.odometer = response["timed_odometer"]["mileage"],
        self.ignition = response["ignition"]["type"]
        self.timestamp = datetime.timestamp(datetime.now())

    def to_dict(self):
        return {
            "battery": self.battery.to_dict(),
            "environment": self.environment.to_dict(),
            "odometer": self.odometer,
            "ignition": self.ignition,
            "position": self.position_state.to_dict(),
            "timestamp": self.timestamp
        }
