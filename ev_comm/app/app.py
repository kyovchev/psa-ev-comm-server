import time
from configparser import ConfigParser

from ev_comm.utils.utils import Singleton
from ev_comm.firebase.firestore_comm import FirestoreComm
from ev_comm.db.db import DB
from ev_comm.psacc_comm.psacc_comm import PsaccComm
from ev_comm.model.car_state import CarState


class App(metaclass=Singleton):
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config/config.ini")

        self.wait_time = int(self.config["APP"]["wait_time"])
        self.firestore_comm = FirestoreComm(
            self.config["FIREBASE"]["certificate_filename"])
        self.db = DB(self.config["DB"]["filename"])
        self.psacc_comm = PsaccComm(
            self.config["PSACC"]["url"], self.config["PSACC"]["vin"])

    def start_app(self):
        car_state = CarState()
        while True:
            try:
                response = self.psacc_comm.getVehicleInfo()
                self.db.save_response(response)

                car_state.load_from_psacc_response(response)
                self.db.save_car_state(car_state)
                self.firestore_comm.store_car_status(car_state)
            except:
                pass

            time.sleep(self.wait_time)
