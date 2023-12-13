#!/usr/bin/env python3
from threading import Thread

from ev_comm.app.app import App


def main():
    app = App()
    t1 = Thread(target=app.start_app,
                args=[], daemon=True)
    t1.start()
    t1.join()


if __name__ == "__main__":
    main()
