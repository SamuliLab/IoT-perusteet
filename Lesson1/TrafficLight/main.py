import time
import machine

time.sleep(0.1) # Wait for USB to become ready

switch = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

ledRed = machine.Pin(15, machine.Pin.OUT)
ledYellow = machine.Pin(14, machine.Pin.OUT)
ledGreen = machine.Pin(13, machine.Pin.OUT)



while True:
    if switch.value() == 1:
        print("Nappi painettu!")
        ledRed.value(1)
        buzzer.value(1)
        time.sleep(10)
        buzzer.value(0)
        ledRed.value(0)

    ledRed.value(1)
    time.sleep(2)
    ledYellow.value(1)
    time.sleep(2)
    ledRed.value(0)
    ledYellow.value(0)
    ledGreen.value(1)
    time.sleep(5)
    ledGreen.value(0)
    ledYellow.value(1)
    time.sleep(2)
    ledYellow.value(0)
    ledRed.value(1)
    time.sleep(5)