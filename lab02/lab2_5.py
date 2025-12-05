from machine import Pin
import time

lr1 = Pin(34, Pin.IN)
lr2 = Pin(35, Pin.IN)

pins = [16, 17, 18, 19]
leds = [Pin(p, Pin.OUT) for p in pins]
delay = 300

def show_pattern(value):
    for bit in range(4):
        bit_value = (value >> bit) & 1  
        leds[bit].value(bit_value) 

def run_led(led, delay):
    for i in range(len(leds)):
        led.on()
        time.sleep_ms(delay)

    for i in range(len(leds)):
        led.off()
        time.sleep_ms(delay)

def blink(led, delay):
    for i in range(len(leds)):
        led.on()

while True:
    if lr1.value() == 1 and lr2.value() == 1:
        for i in range(len(leds)):
            blink(leds[i], delay)

    elif lr1.value() == 1 and lr2.value() == 0:
        for i in range(len(leds)):
            run_led(leds[i], delay)

    elif lr1.value() == 0 and lr2.value() == 1:
        for i in range(len(leds) -1, -1, -1):
            run_led(leds[i], delay)

    else:
        for v in range(0, 16): 
            show_pattern(v)
            time.sleep_ms(delay)

        for v in range(14, 0, -1):  
            show_pattern(v)
            time.sleep_ms(delay)
        



