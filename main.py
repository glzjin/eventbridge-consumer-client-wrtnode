import requests
import time
from event import Event
from config import Config

def get_event():
    try:
        response = requests.get(Config.url + "/consumer/" + Config.consumer_uuid + "/event", params = {"key": Config.consumer_key})
        data = response.json()
        if data['code'] == 100:
            new_event = Event(data['data']['event']['event_id'])
            return new_event
        else:
            return None
    except Exception:
        return None

print("Booted!")
while True:
    event = get_event()

    if event:
        event.consume()
        print("Event ID:" + str(event.event_id) + " Consumed!")
    time.sleep(1)
