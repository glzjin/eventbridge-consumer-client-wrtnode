import logging
from config import Config

class Event:
    event_id = 0
    def __init__(self, event_id):
        self.event_id = event_id

    def consume(self):
        if self.event_id in Config.event_list:
            logging.info("Found event ID " + str(self.event_id) + "!")
            Config.event_list[self.event_id]()
