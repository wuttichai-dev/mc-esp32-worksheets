from machine import Pin
import time

led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)
sw1  = Pin(13, Pin.IN, Pin.PULL_UP)
sw2  = Pin(14, Pin.IN, Pin.PULL_UP)

delay = 200

def blink(led, n):
    for _ in range(n):
        led.on()
        time.sleep_ms(delay)
        led.off()
        time.sleep_ms(delay)

while True:
    s1, s2 = sw1.value(), sw2.value()

    if s1 == 0 and s2 == 1:
        blink(led1, 3)
    elif s1 == 1 and s2 == 0:
        blink(led2, 5)
    else:
        led1.on()
        led2.on()
