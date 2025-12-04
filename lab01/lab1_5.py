from machine import Pin
import time

led_pins = [16, 17, 18, 19]

leds = [Pin(p, Pin.OUT) for p in led_pins]

delay = 300  

def show_pattern(value):
    for bit in range(4):
        bit_value = (value >> bit) & 1  
        leds[bit].value(bit_value)      

while True:
    for v in range(0, 16): 
        show_pattern(v)
        time.sleep_ms(delay)

    for v in range(14, 0, -1):  
        show_pattern(v)
        time.sleep_ms(delay)