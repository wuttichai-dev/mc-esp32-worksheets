from machine import Pin
import time

leds = [Pin(p, Pin.OUT) for p in (16, 17, 18, 19)]

rows = [Pin(p, Pin.OUT) for p in (21, 22, 23, 25)]
cols = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (26, 27, 32, 33)]

keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D'],
]

while True:
    key = None

    for r in range(4):

        for i in range(4):
            rows[i].value(1)

        rows[r].value(0)
        time.sleep_us(50)

        for c in range(4):
            if cols[c].value() == 0:
                key = keys[r][c]

    if key in ['1', '2', '3', '4']:

        for led in leds:
            led.value(0)

        index = int(key) - 1
        leds[index].value(1)

    elif key == '0':

        for led in leds:
            led.value(0)

    time.sleep_ms(50)
