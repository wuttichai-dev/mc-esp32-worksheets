from machine import Pin
import time

led01 = Pin(16, Pin.OUT)
sw1 = Pin(13, Pin.IN, Pin.PULL_UP)

while True:
    sw = sw1.value()
    if sw == 0:
        led01.on()
    else:
        led01.off()