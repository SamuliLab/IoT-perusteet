import time
import machine

time.sleep(0.1) # Wait for USB to become ready

switch = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(18, machine.Pin.OUT)


while True:
    if switch.value():
        led.value(False)
    else:
        led.value(True)