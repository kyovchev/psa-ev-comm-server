from tinydb import TinyDB


class DB:
    def __init__(self, filename):
        self.db = TinyDB(filename)

    def save_response(self, response):
        self.db.table("responses").insert(response)

    def save_car_state(self, car_state):
        self.db.table("car_states").insert(car_state.to_dict())
