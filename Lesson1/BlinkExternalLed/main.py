import time
import machine

time.sleep(0.1) # Wait for USB to become ready

ledi = machine.Pin("LED", machine.Pin.OUT)

while True:
  ledi.value(True)
  time.sleep(1)
  ledi.value(False)
  time.sleep(1)