import websocket
import threading
import time
from event import Event
from config import Config
import logging
import json
import sys

# 初始化日志
logging.basicConfig()
root_logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s %(message)s', '%m/%d/%Y %I:%M:%S %p')
root_logger.handlers[0].formatter = formatter
root_logger.level = logging.INFO


#Websocket 获取
def on_message(ws, message):
    data = json.loads(message)
    if data['code'] == 300:
        # 处理事件
        new_event = Event(data['data']['event']['event_id'])
        logging.info("Event ID:" + str(new_event.event_id) + " Consuming!")

        event_thread = threading.Thread(target = new_event.consume)
        event_thread.start()

        logging.info("Event ID:" + str(new_event.event_id) + " Consumed!")

def keep_alive():
    logging.info("Main Keep Alive!")
    ws.send(json.dumps({'action': 'ping'}))

    # 保活定时器
    global t
    t = threading.Timer(60, keep_alive)
    t.start()

def on_close(ws):
    logging.info( "### closed ###")

def on_open(ws):
    # 注册
    ws.send(json.dumps({'action': 'reg', 'consumer_uuid': Config.consumer_uuid, 'key': Config.consumer_key}))

    # 连接保活
    keep_alive()


if __name__ == "__main__":
    try:
        logging.info("Booted!")
        # websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://eb.zhaoj.in/consumer/websocket",
                                  on_message = on_message,
                                  on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()
    except KeyboardInterrupt:
        logging.info("Exiting!")
        t.cancel()
        ws.close()
        sys.exit(1)



# # 旧方法
# def get_event():
#     try:
#         response = session.get(Config.url + "/consumer/" + Config.consumer_uuid + "/event", params = {"key": Config.consumer_key})
#         data = response.json()
#         if data['code'] == 100:
#             new_event = Event(data['data']['event']['event_id'])
#             return new_event
#         else:
#             return None
#     except Exception:
#         return None
#
# logging.info("Booted!")
# while True:
#     event = get_event()
#
#     if event:
#         try:
#             event.consume()
#             logging.info("Event ID:" + str(event.event_id) + " Consumed!")
#         except Exception:
#             import traceback
#             traceback.print_exc(file=sys.stdout)
#
#             logging.info("Event ID:" + str(event.event_id) + " Consume failed!")
#     time.sleep(1)
