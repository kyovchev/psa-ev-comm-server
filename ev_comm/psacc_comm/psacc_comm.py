import requests
import json
from datetime import datetime


class PsaccComm:
    def __init__(self, config):
        self.url = config["url"]
        self.vin = config["vin"]
        self.connection_timeout = int(config["connection_timeout"])

    def getVehicleInfo(self):
        url = f"{self.url}/get_vehicleinfo/{self.vin}"
        res = requests.get(url, timeout=self.connection_timeout)
        response = json.loads(res.text)
        response["timestamp"] = datetime.timestamp(datetime.now())

        return response
