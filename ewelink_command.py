import requests
import json
import ssl
import logging
from websocket import create_connection
import time
import threading

class Ewelink:
    data = None

    def __init__(self, config_class):
        self.config_class = config_class
        self.get_ewelink_device_info()
        self.init_api_ws()

    def __del__(self):
        self.close_api_ws()

    def close_api_ws(self):
        self.ws.close()

    def init_api_ws(self):
        millisecond_unix_timestamp = time.time() * 1000
        self.ws = create_connection("wss://cn-long.coolkit.cc:8080/api/ws",
                                    sslopt={"cert_reqs": ssl.CERT_NONE})
        self.ws.send(json.dumps({"action": "userOnline", "version": 6, "imei": "1234567890", \
                                "ts": int(millisecond_unix_timestamp / 1000), "model": "iphone6", "os": "ios", "romVersion": "9", \
                                "at": self.config_class.access_token, "userAgent": "app", "apikey": self.config_class.api_key, \
                                "appid" : "EMasBJoZukhIA5STUb18ZrDG6jCBMkuu", "nonce": "2moes82f", "sequence":int(millisecond_unix_timestamp), "apkVesrion": "1.8"}))
        self.keep_alive()

    def keep_alive(self):
        self.ws.send("ping")
        logging.info('Ewelink DID: ' + self.config_class.device_id + ' Keep alive!')

        # 定时器
        global timer
        timer = threading.Timer(110, self.keep_alive)
        timer.start()

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
            self.ws.send(json.dumps(self.set_target_status(data, index, True)))
        else:
            self.ws.send(json.dumps(self.set_target_status(data, index, False)))
