from machine import Pin
import time

led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)

while True:
    led1.on()
    led2.off()
    time.sleep_ms(200)

    led1.off()
    led2.on()
    time.sleep_ms(200)