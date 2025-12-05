from machine import Pin
import time

lr = Pin(34, Pin.IN)
led = Pin(16, Pin.OUT)

while True:
    if lr.value() == 0:
        led.on()
    else:
        led.off()