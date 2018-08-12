import event_consume

class Event:
    event_id = 0
    def __init__(self, event_id):
        self.event_id = event_id

    def consume(self):
        event_consume.event_consume(self.event_id)
