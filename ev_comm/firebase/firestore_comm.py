import firebase_admin
from firebase_admin import credentials, firestore, messaging


class FirestoreComm:
    def __init__(self, certificate_filename):
        cred = credentials.Certificate(certificate_filename)

        self.app = firebase_admin.initialize_app(cred)

        self.firebase_db = firestore.client()

    def store_car_status(self, car_state):
        self.firebase_db.collection("car_status").document(
            "current").set(car_state.to_dict())

    def send_battery_status(self, percentage):
        docs = self.firebase_db.collection("fcm").stream()

        for doc in docs:
            d = doc.to_dict()
            message = messaging.Message(
                data={
                    "title": "EV",
                    "body": f"Battery level: {percentage}%",
                },
                token=d["token"],
            )
            messaging.send(message)
