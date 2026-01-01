from machine import Pin
import time

pins = [16, 17, 18, 19]
leds = [Pin(p, Pin.OUT) for p in pins]

sw1 = Pin(13, Pin.IN, Pin.PULL_UP)
sw2 = Pin(14, Pin.IN, Pin.PULL_UP)

def run_led(led, delay):
    led.on()
    time.sleep_ms(delay)
    led.off()
    time.sleep_ms(delay)

while True:
    if sw1.value() == 0 and sw2.value() ==1:
        for i in range(len(leds)):
            run_led(leds[i], 200)
    
    elif sw1.value() == 1 and sw2.value() ==0:
        for i in range(len(leds) -1, -1, -1):
            run_led(leds[i], 200)
    
    else:
        for led in leds:
            led.on()
        time.sleep_ms(200)
        for led in leds:
            led.off()
        time.sleep_ms(200)