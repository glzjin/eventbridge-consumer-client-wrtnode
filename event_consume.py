from config import Config

def event_consume(event_id):
    if event_id in Config.event_list:
        print("Found event!")
        Config.event_list[event_id]()
