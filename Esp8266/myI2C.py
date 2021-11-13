from machine import Pin, I2C
import time
import ustruct

def initI2C():
    # construct an I2C bus
    return I2C(scl=Pin(5), sda=Pin(4), freq=100000)

def readI2CRegister24bit(i2c,adr,reg):
    buf = bytearray(1)
    buf[0] = reg

    i2c.writeto(adr,buf)
    time.sleep_ms(20)
    buf = i2c.readfrom(adr,3)

    return ustruct.unpack(">I",bytes(1)+buf)[0]

def readI2CRegister24bitS(i2c,adr,reg):
    buf = bytearray(1)
    buf[0] = reg

    i2c.writeto(adr,buf)
    time.sleep_ms(20)
    buf = i2c.readfrom(adr,3)

    return ustruct.unpack(">i",bytes(1)+buf)[0]

def readI2CRegister16bit(i2c,adr,reg):
    buf = bytearray(1)
    buf[0] = reg

    i2c.writeto(adr,buf)
    time.sleep_ms(20)
    buf = i2c.readfrom(adr,2)

    return ustruct.unpack(">H",buf)[0]

def readI2CRegister16bitS(i2c,adr,reg):
    buf = bytearray(1)
    buf[0] = reg

    i2c.writeto(adr,buf)
    time.sleep_ms(20)
    buf = i2c.readfrom(adr,2)

    return ustruct.unpack(">h",buf)[0]

def readI2CRegister16bitLE(i2c,adr,reg):
    buf = bytearray(1)
    buf[0] = reg

    i2c.writeto(adr,buf)
    time.sleep_ms(20)
    buf = i2c.readfrom(adr,2)

    return ustruct.unpack("<H",buf)[0]

def readI2CRegister16bitSLE(i2c,adr,reg):
    buf = bytearray(1)
    buf[0] = reg

    i2c.writeto(adr,buf)
    time.sleep_ms(20)
    buf = i2c.readfrom(adr,2)

    return ustruct.unpack("<h",buf)[0]

def readI2CRegister8bit(i2c,adr,reg):
    buf = bytearray(1)
    buf[0] = reg

    i2c.writeto(adr,buf)
    time.sleep_ms(20)
    buf = i2c.readfrom(adr,1)

    return ustruct.unpack(">B",buf)[0]

def readI2CRegister8bitS(i2c,adr,reg):
    buf = bytearray(1)
    buf[0] = reg

    i2c.writeto(adr,buf)
    time.sleep_ms(20)
    buf = i2c.readfrom(adr,1)

    return ustruct.unpack(">b",buf)[0]

def writeI2CRegister8bit(i2c,adr, u8Reg, u8Data):
        buf = bytearray(2)
        buf[0] = u8Reg
        buf[1] = u8Data

        i2c.writeto(adr,buf)