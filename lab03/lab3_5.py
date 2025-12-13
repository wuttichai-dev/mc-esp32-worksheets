from machine import Pin
import time

leds = [Pin(p, Pin.OUT) for p in (16, 17, 18, 19)]

def leds_all(on_off):

    for led in leds:
        led.value(on_off)

def blink_error(times=3):

    for _ in range(times):
        leds_all(0)
        time.sleep_ms(200)
        leds_all(1)
        time.sleep_ms(200)
    leds_all(0)

leds_all(0)  

rows = [Pin(p, Pin.OUT) for p in (21, 22, 23, 25)]
cols = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (26, 27, 32, 33)]

keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D'],
]

def scan_key():

    for r in range(4):

        for i in range(4):
            rows[i].value(1)

        rows[r].value(0)
        time.sleep_us(50)

        for c in range(4):
            if cols[c].value() == 0:  
                return keys[r][c]

    return None

PASSWORD = ['1', '2', '3', '4']
input_code = []   

print("Ready... ใส่รหัส 4 หลักด้วย keypad")

while True:
    k = scan_key()

    if k is not None:
        print("กดปุ่ม:", k)

        input_code.append(k)
        print("input_code =", input_code)

        while scan_key() is not None:
            time.sleep_ms(20)

        if len(input_code) == 4:
            if input_code == PASSWORD:
                print("รหัสถูกต้อง!")
                leds_all(1)          
                time.sleep(1)        
                leds_all(0)
            else:
                print("รหัสผิด!")
                blink_error(3)       

            input_code = []

    time.sleep_ms(20)
