import rf_command

def key1_press():
    rf_command.send_rf_command(0)

def key1_learn():
    rf_command.send_rf_command(0, is_study = True)

def key2_press():
    rf_command.send_rf_command(1)

def key2_learn():
    rf_command.send_rf_command(1, is_study = True)

def key3_press():
    rf_command.send_rf_command(2)

def key3_learn():
    rf_command.send_rf_command(2, is_study = True)

def key4_press():
    rf_command.send_rf_command(3)

def key4_learn():
    rf_command.send_rf_command(3, is_study = True)

class Config:
    #服务器的 URL
    url = "http://eb.zhaoj.in"
    #消费者角色的 Key
    consumer_key = "123"
    #消费者角色的 UUID
    consumer_uuid = "uuid"
    #事件表
    event_list = {1: key1_press, 2: key2_press, \
                3: key3_press, 4: key4_press, \
                5: key1_learn, 6: key2_learn, \
                7: key3_learn, 8: key4_learn}
