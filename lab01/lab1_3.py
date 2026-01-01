from machine import Pin
import time

pins = [16, 17, 18, 19]
leds = [Pin(p, Pin.OUT) for p in pins]

def led_run(led, delay):
    led.on()
    time.sleep_ms(delay)
    led.off()
    time.sleep_ms

while True:
    for i in range(len(leds)):
        led_run(leds[i], 300)

    for i in range(len(leds) -2, 0, -1):
        led_run(leds[i], 300)

                   