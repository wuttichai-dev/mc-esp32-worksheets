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

    if key is not None and key in '0123456789':
        n = int(key)   

        for i in range(4):
            bit = (n >> (3 - i)) & 1   
            leds[i].value(bit)

        print("Key:", key, "Value:", n, "Binary:", "{:04b}".format(n))

    time.sleep_ms(50)
