import requests
import json
import logging
import websocket
import time
import threading
import ssl

class Ewelink(websocket.WebSocketApp):
    data = None

    def __init__(self, config_class, access_token = ''):
        self.config_class = config_class
        self.get_ewelink_device_info()
        super(Ewelink, self).__init__("wss://cn-long.coolkit.cc:8080/api/ws")
        self.ws_init()

    def __del__(self):
        self.close_api_ws()
        super(Ewelink, self).__del__()

    def ws_run(self):
        self.running = True
        while self.running:
            try:
                self.run_forever(sslopt = {"cert_reqs": ssl.CERT_NONE}, ping_interval = 10)
            except KeyboardInterrupt:
                self.running = False
                self.close()

    def ws_init(self):
        self.thread = threading.Thread(target = self.ws_run)
        self.thread.start()

    def close_api_ws(self):
        self.running = False

    def on_error(self, error):
        logging.error(error)

    def on_message(self, message):
        data = json.loads(message)

        if 'deviceid' in data:
            if data['deviceid'] == self.config_class.device_id:
                if 'params' in data:
                    if 'switches' in data['params']:
                        self.data = data['params']['switches']

    def on_open(self):
        millisecond_unix_timestamp = time.time() * 1000
        self.send(json.dumps({"action": "userOnline", "version": 6, "imei": "1234567890", \
                                "ts": int(millisecond_unix_timestamp / 1000), "model": "iphone6", "os": "ios", "romVersion": "9", \
                                "at": self.config_class.access_token, "userAgent": "app", "apikey": self.config_class.api_key, \
                                "appid" : "oeVkj2lYFGnJu5XUtWisfW4utiN4u9Mq", "nonce": "2moes82f", "sequence":int(millisecond_unix_timestamp), "apkVesrion": "1.8"}))

    def get_ewelink_device_info(self):
        if self.data is not None:
            return self.data

        response = requests.get("https://cn-api.coolkit.cc:8080/api/user/device",  \
                                params = {'version': 6, 'romVersion': 9, 'os': 'ios', 'model': 'iphone6', \
                                        'lang': 'cn', 'imei': '1234567890', 'getTags': 1, \
                                        'appVersion': '9.9.9'}, \
                                headers = {'Authorization': 'Bearer ' + self.config_class.access_token})

        for device_info in response.json()['devicelist']:
            if device_info['deviceid'] == self.config_class.device_id:
                self.data = device_info['params']['switches']
                return self.data

    def get_target_status(self, params, index):
        if params[index]['switch'] == 'on':
            return True
        else:
            return False

    def set_target_status(self, params, index, is_on = False):
        millisecond_unix_timestamp = time.time() * 1000
        if is_on:
            params[index]['switch'] = 'on'
        else:
            params[index]['switch'] = 'off'

        self.data = params

        return {"action": "update", "userAgent": "app", "apikey": self.config_class.api_key, \
                "deviceid": self.config_class.device_id, "params": {'switches': params}, "sequence": int(millisecond_unix_timestamp)}

    def button_press(self, index = 0):
        data = self.get_ewelink_device_info()
        if self.get_target_status(data, index):
            self.button_set_status(index, False)
        else:
            self.button_set_status(index, True)


    def button_set_status(self, index = 0, is_on = False):
        data = self.get_ewelink_device_info()
        if is_on:
            self.send(json.dumps(self.set_target_status(data, index, True)))
        else:
            self.send(json.dumps(self.set_target_status(data, index, False)))
