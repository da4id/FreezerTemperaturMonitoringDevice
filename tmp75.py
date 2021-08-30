import time
from machine import Pin, I2C

import myI2C


def init(i2cObj, adr):
    buf = bytearray(2)
    # write config
    buf[0] = 0x01
    # configValue
    buf[1] = 0x60

    i2cObj.writeto(adr, buf)

    # read Temperature
    buf = bytearray(1)
    buf[0] = 0x00

    i2cObj.writeto(adr, buf)


def readValue(i2cObj, adr):
    temp = i2cObj.readfrom(adr, 2)

    t = temp[0] + temp[1] / 256
    return t


def getBoardTemperature():
    i2c = myI2C.initI2C()
    init(i2c, 0x49)
    time.sleep_ms(300)
    return readValue(i2c, 0x49)


def readTemperature(adr):
    i2c = myI2C.initI2C()
    init(i2c, adr)
    time.sleep_ms(300)
    return readValue(i2c, adr)
