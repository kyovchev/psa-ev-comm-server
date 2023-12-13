import requests
import json
from datetime import datetime


class PsaccComm:
    def __init__(self, url, vin):
        self.url = url
        self.vin = vin

    def getVehicleInfo(self):
        url = f"{self.url}/get_vehicleinfo/{self.vin}"
        res = requests.get(url)
        response = json.loads(res.text)
        response["timestamp"] = datetime.timestamp(datetime.now())

        return response
