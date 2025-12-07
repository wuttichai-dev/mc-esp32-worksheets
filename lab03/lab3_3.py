from machine import Pin
import time

# ---------- LED 4 ดวง ----------
# กำหนดให้ leds[0] = บิตตัวซ้ายสุด (MSB)
#           leds[3] = บิตตัวขวาสุด (LSB)
leds = [Pin(p, Pin.OUT) for p in (16, 17, 18, 19)]

# ---------- ขา keypad ----------
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

    # ---------- สแกน keypad ----------
    for r in range(4):
        # ตั้งทุก row = 1 ก่อน
        for i in range(4):
            rows[i].value(1)

        # ดึง row ที่กำลังตรวจให้เป็น 0
        rows[r].value(0)
        time.sleep_us(50)

        # ตรวจทุก column
        for c in range(4):
            if cols[c].value() == 0:   # มีปุ่มถูกกด
                key = keys[r][c]

    # ---------- แสดงเลขฐานสองบน LED ----------
    if key is not None and key in '0123456789':
        n = int(key)   # แปลง '0'..'9' เป็นตัวเลข 0..9

        # แปลงเป็น 4 บิต แล้วส่งไปที่ LED
        # ตัวอย่าง: n = 5 -> 0101
        for i in range(4):
            bit = (n >> (3 - i)) & 1   # ดึงบิตจากซ้ายไปขวา
            leds[i].value(bit)

        print("Key:", key, "Value:", n, "Binary:", "{:04b}".format(n))

    # ถ้ากด A B C D * # -> ไม่ทำอะไร

    time.sleep_ms(50)
