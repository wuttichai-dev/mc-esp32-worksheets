from machine import Pin
import time

lr1 = Pin(34, Pin.IN)
led = Pin(16, Pin.OUT)

while True:
    if lr1.value() == 0:
        led.on()
    else:
        led.off()