# PSA EV Communicator App

This app fetches data from a [PSA Car Controller](https://github.com/flobz/psa_car_controller) server.

The response is stored into local database and into a Firestore.

The Firestore data is used by Next.js ReactJS front-end app located at [https://ev-psa.web.app](https://ev-psa.web.app).

In order to use it you have to setup your PSA Car Controller server.

Also, you will have to create a config.ini file into the config directory.