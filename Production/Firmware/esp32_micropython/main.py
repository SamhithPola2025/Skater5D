from machine import I2C, Pin
from time import sleep
import mpu6050
import ujson
import sys

i2c = I2C(0, scl=Pin(5), sda=Pin(6))
mpu = mpu6050.accel(i2c)

while True:
    accel = mpu.get_values()
    data = {
        "ax": accel['AcX'],
        "ay": accel['AcY'],
        "az": accel['AcZ'],
        "gx": accel['GyX'],
        "gy": accel['GyY'],
        "gz": accel['GyZ'],
    }
    sys.stdout.write(ujson.dumps(data) + "\n")
    sleep(0.02)