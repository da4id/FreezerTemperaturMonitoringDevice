import machine
from machine import RTC
from machine import Pin
import time


def reboot():
    machine.reset()

def sleepMinutes(minutes):
    print("sleep for " + str(minutes) + " minutes")
    # configure RTC.ALARM0 to be able to wake the device
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    # set RTC.ALARM0 to fire after 10 seconds (waking the device)
    rtc.alarm(rtc.ALARM0, minutes * 1000 * 60)

    # put the device to sleep
    machine.deepsleep()


def keepOn():
    pinKeepOn = Pin(14, Pin.IN)
    if pinKeepOn.value() == 1:
        return True
    return False
