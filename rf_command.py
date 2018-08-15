import serial
import struct

rf_channel_list = [b"\x01", b"\x02", b"\x03", b"\x04"]

def send_rf_command(config_class, channel, is_study = False):
    ser = serial.Serial(
        port = config_class.tty,
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS
    )

    ser.flushInput()
    ser.flushOutput()

    if is_study:
        data = b"\xAA"
    else:
        data = b"\xBB"

    data += rf_channel_list[channel]

    data += b"\xFF"

    ser.write(data)

    ser.flushInput()
    ser.flushOutput()

    ser.close()
