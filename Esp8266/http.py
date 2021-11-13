import network
import socket
import time
import urequests


def waitUntilConnected():
    print("Wait for connection")
    sta_if = network.WLAN(network.STA_IF)
    i = 0
    while sta_if.isconnected() == False:
        i = i + 1
        if i == 300:
            print("Connection Timeout")
            raise Exception("Connection Timeout")
        time.sleep_ms(100)
    print("Connected")


def http_post(url, data):
    waitUntilConnected()
    i = 0
    while i < 300:
        i = i + 1
        r = urequests.post(url, data=data)
        print(r.status_code)
        if r.status_code == 200:
            print(r.text)
            return

def http_get(url):
    waitUntilConnected()
    i = 0
    while i < 300:
        i = i + 1
        r = urequests.get(url)
        print(r.status_code)
        if r.status_code == 200:
            print(r.text)
            return r.text
