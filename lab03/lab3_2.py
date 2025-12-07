from machine import Pin
import time

# LED 4 ดวง
leds = [Pin(p, Pin.OUT) for p in (16, 17, 18, 19)]

# ขา keypad
rows = [Pin(p, Pin.OUT) for p in (21, 22, 23, 25)]
cols = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (26, 27, 32, 33)]

# แผนผังปุ่มบน keypad 4x4
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D'],
]

while True:
    key = None

    # สแกนหาปุ่มที่กด
    for r in range(4):
        # ให้ทุก row เป็น 1 ก่อน
        for i in range(4):
            rows[i].value(1)

        # ดึง row ที่กำลังตรวจให้เป็น 0
        rows[r].value(0)
        time.sleep_us(50)

        # เช็คทุก column
        for c in range(4):
            if cols[c].value() == 0:
                key = keys[r][c]

    # ถ้ามีปุ่มถูกกด
    if key in ['1', '2', '3', '4']:
        # ดับทุกดวงก่อน
        for led in leds:
            led.value(0)
        # เลือกให้ดวงที่ n ติด (index = n-1)
        index = int(key) - 1
        leds[index].value(1)

    elif key == '0':
        # ปุ่ม 0 ดับทุกดวง
        for led in leds:
            led.value(0)

    time.sleep_ms(50)
