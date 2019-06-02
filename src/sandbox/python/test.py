
import network
import machine
import sys
import time

# enable station interface and connect to WiFi access point


def openAP():
    nic = network.WLAN(network.AP_IF)
    nic.active(True)


def connectSTA(name, psk):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(name, psk)
    while not sta_if.isconnected():
        pass
    print("CONNECTED")


def ccc():
    connectSTA('marxworld', 'wunedowe')


def lll():
    while (True):
        print("TEST")
        sleep(0.5)


def reset():
    machine.reset()
