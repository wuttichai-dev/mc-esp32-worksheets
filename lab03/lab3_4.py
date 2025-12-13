from machine import Pin
import time

led_pins = (16, 17, 18, 19)
leds = [Pin(p, Pin.OUT) for p in led_pins]

def clear_leds():
    for led in leds:
        led.value(0)

clear_leds()

rows = [Pin(p, Pin.OUT) for p in (21, 22, 23, 25)]
cols = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (26, 27, 32, 33)]

key_map = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D'],
]

key_to_value = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    '*': 14,
    '#': 15,
}

def scan_key():

    for r, prow in enumerate(rows):
        
        for pr in rows:
            pr.value(1)

        prow.value(0)
        time.sleep_us(50)  

        for c, pcol in enumerate(cols):
            if pcol.value() == 0:  
                return key_map[r][c]

    return None

def show_number_on_leds(n):

    n &= 0xF  
    for i in range(4):
        bit = (n >> (3 - i)) & 1
        leds[i].value(bit)

print("Ready... กดปุ่มบน keypad ได้เลย")

while True:
    k = scan_key()
    if k is not None:
        print("Key pressed:", k)

        if k in key_to_value:
            n = key_to_value[k]
            show_number_on_leds(n)
            print("Value:", n, "Binary: {:04b}".format(n))

        while scan_key() is not None:
            time.sleep_ms(20)

    time.sleep_ms(20)
