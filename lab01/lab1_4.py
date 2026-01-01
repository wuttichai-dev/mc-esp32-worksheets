from machine import Pin
import time

pins = [16, 17, 18, 19]
leds = [Pin(p, Pin.OUT) for p in pins]

patterns = [
    (),
    (0,),
    (0, 1),
    (1, 2),
    (2, 3),
    (3,),
    ()
]

while True:
    for pat in patterns:
        for i, led in enumerate(leds):
            led.value(1 if i in pat else 0)
        time.sleep_ms(500)
