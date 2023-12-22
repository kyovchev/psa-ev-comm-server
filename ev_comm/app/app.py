import os
import requests
import time
from configparser import ConfigParser

from ev_comm.utils.utils import Singleton
from ev_comm.firebase.firestore_comm import FirestoreComm
from ev_comm.db.db import DB
from ev_comm.psacc_comm.psacc_comm import PsaccComm
from ev_comm.model.car_state import CarState


MAX_RETRIES = 3


class App(metaclass=Singleton):
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config/config.ini")

        self.wait_time = int(self.config["APP"]["wait_time"])
        self.firestore_comm = FirestoreComm(
            self.config["FIREBASE"]["certificate_filename"])
        self.db = DB(self.config["DB"]["filename"])
        self.psacc_comm = PsaccComm(self.config["PSACC"])

        self.last_battery_level_notification = -1

        self.retries = 0
        self.alerted = False

    def start_app(self):
        car_state = CarState()
        while True:
            try:
                response = self.psacc_comm.getVehicleInfo()
                self.db.save_response(response)
                car_state.load_from_psacc_response(response)
                self.db.save_car_state(car_state)
                self.firestore_comm.store_car_status(car_state)

                if car_state.battery.level != self.last_battery_level_notification \
                        and car_state.battery.level % 10 == 0:
                    self.firestore_comm.send_battery_status(
                        car_state.battery.level)
                    self.last_battery_level_notification = car_state.battery.level
                if car_state.battery.level > self.last_battery_level_notification:
                    self.last_battery_level_notification = car_state.battery.level

                self.retries = 0
                self.alerted = False
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
                self.retries = self.retries + 1
                if not self.alerted and self.retries == MAX_RETRIES:
                    self.firestore_comm.notify_conn_error(
                        "PSACC Connection Timeout!")
                    self.alerted = True
                    os.system(
                        f"sudo /usr/bin/systemctl restart {self.config['PSACC']['service']}")
            except:
                pass

            time.sleep(self.wait_time)
