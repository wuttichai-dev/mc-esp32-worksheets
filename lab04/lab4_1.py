from machine import Pin
import time

pins = [4, 5, 13, 14, 16, 17, 18, 19]
segment  = [Pin(p, Pin.OUT) for p in pins]

ON, OFF = 0, 1

hex7b = [
    0x3F, 
    0x06, 
    0x5B, 
    0x4F, 
    0x66, 
    0x6D, 
    0x7D, 
    0x07, 
    0x7F, 
    0x6F, 
    0x77, 
    0x7C, 
    0x39, 
    0x5E, 
    0x79, 
    0x71  
]

def show(n):
    m = hex7b[n & 0xF]
    for i in range(7):  
        segment[i].value(ON if (m >> i) & 1 else OFF)
    segment[7].value(OFF)   

while True:
    for n in range(16):
        show(n)
        time.sleep(0.5)
