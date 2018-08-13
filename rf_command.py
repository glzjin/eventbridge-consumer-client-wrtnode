import serial
import struct

rf_channel_list = ["\x01", "\x02", "\x03", "\x04"]

def send_rf_command(channel, is_study = False):
    ser = serial.Serial(
        port = '/dev/ttyUSB0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS
    )

    if is_study:
        data = "\xAA"
    else:
        data = "\xBB"

    data += rf_channel_list[channel]

    data += "\xFF"

    ser.write(data)

    ser.flushInput()
    ser.flushOutput()

    ser.close()
