import rf_command
from ewelink_command import Ewelink

# 有几个设备就创建一个
# 红外的
class RfConfig:
    tty = '/dev/ttyUSB0'

    def key1_press():
        rf_command.send_rf_command(RfConfig, 0)

    def key1_learn():
        rf_command.send_rf_command(RfConfig, 0, is_study = True)

    def key2_press():
        rf_command.send_rf_command(RfConfig, 1)

    def key2_learn():
        rf_command.send_rf_command(RfConfig, 1, is_study = True)

    def key3_press():
        rf_command.send_rf_command(RfConfig, 2)

    def key3_learn():
        rf_command.send_rf_command(RfConfig, 2, is_study = True)

    def key4_press():
        rf_command.send_rf_command(RfConfig, 3)

    def key4_learn():
        rf_command.send_rf_command(RfConfig, 3, is_study = True)

# 易微联
class Ewelink1Config:
    # AppKey
    api_key = ""

    # AccessToken
    access_token = ""

    # Device id
    device_id = ""

    def __init__(self):
        self.ewelink = Ewelink(Ewelink1Config)

    def switch1_press(self):
        self.ewelink.button_press(0)

    def switch1_on(self):
        self.ewelink.button_set_status(0, True)

    def switch1_off(self):
        self.ewelink.button_set_status(0, False)

    def switch2_press(self):
        self.ewelink.button_press(1)

    def switch2_on(self):
        self.ewelink.button_set_status(1, True)

    def switch2_off(self):
        self.ewelink.button_set_status(1, False)

class Ewelink2Config:

    # AppKey
    api_key = ""

    # AccessToken
    access_token = ""

    # Device id
    device_id = ""

    def __init__(self):
        self.ewelink = Ewelink(Ewelink2Config)

    def switch1_press(self):
        self.ewelink.button_press(0)

    def switch1_on(self):
        self.ewelink.button_set_status(0, True)

    def switch1_off(self):
        self.ewelink.button_set_status(0, False)

    def switch2_press(self):
        self.ewelink.button_press(1)

    def switch2_on(self):
        self.ewelink.button_set_status(1, True)

    def switch2_off(self):
        self.ewelink.button_set_status(1, False)

    def switch3_press(self):
        self.ewelink.button_press(2)

    def switch3_on(self):
        self.ewelink.button_set_status(2, True)

    def switch3_off(self):
        self.ewelink.button_set_status(2, False)

    def switch4_press(self):
        self.ewelink.button_press(3)

    def switch4_on(self):
        self.ewelink.button_set_status(3, True)

    def switch4_off(self):
        self.ewelink.button_set_status(3, False)

class Config:
    # 服务器的 URL
    url = "http://eb.zhaoj.in"
    # 消费者角色的 Key
    consumer_key = ""
    # 消费者 UUID
    consumer_uuid = ""
    # 事件表
    event_list = {1: RfConfig.key1_press, 2: RfConfig.key2_press, \
                3: RfConfig.key3_press, 4: RfConfig.key4_press, \
                5: RfConfig.key1_learn, 6: RfConfig.key2_learn, \
                7: RfConfig.key3_learn, 8: RfConfig.key4_learn}

    ewelink1 = Ewelink1Config()
    event_list.update({9: ewelink1.switch1_press, 10: ewelink1.switch1_on, \
                    11: ewelink1.switch1_off, 12: ewelink1.switch2_press, \
                    13: ewelink1.switch2_on, 14: ewelink1.switch2_off})

    ewelink2 = Ewelink2Config()
    event_list.update({15: ewelink2.switch1_press, 16: ewelink2.switch1_on, \
                    17: ewelink2.switch1_off, 18: ewelink2.switch2_press, \
                    19: ewelink2.switch2_on, 20: ewelink2.switch2_off, \
                    21: ewelink2.switch3_press, 22: ewelink2.switch3_on, \
                    23: ewelink2.switch3_off, 24: ewelink2.switch4_press, \
                    25: ewelink2.switch4_on, 26: ewelink2.switch4_off})
