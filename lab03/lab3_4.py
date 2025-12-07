from machine import Pin
import time

# ---------- ตั้งค่า LED 4 ดวง ----------
# สมมติ: leds[0] = บิต MSB, leds[3] = บิต LSB
led_pins = (16, 17, 18, 19)
leds = [Pin(p, Pin.OUT) for p in led_pins]

def clear_leds():
    for led in leds:
        led.value(0)

clear_leds()

# ---------- ตั้งค่า keypad ----------
# rows = OUTPUT, cols = INPUT + PULL_UP
rows = [Pin(p, Pin.OUT) for p in (21, 22, 23, 25)]
cols = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (26, 27, 32, 33)]

# แผนผัง keypad แบบมาตรฐาน 4x4:
#  [ [1] [2] [3] [A] ]
#  [ [4] [5] [6] [B] ]
#  [ [7] [8] [9] [C] ]
#  [ [*] [0] [#] [D] ]
key_map = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D'],
]

# mapping ปุ่ม → ค่าตัวเลข 0–15
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

# ---------- ฟังก์ชันสแกน keypad ----------
def scan_key():
    """คืนค่าเป็นตัวอักษรของปุ่มที่กด หรือ None ถ้าไม่กด"""
    for r, prow in enumerate(rows):
        # ปล่อยทุก row เป็น HIGH
        for pr in rows:
            pr.value(1)

        # ดึง row นี้ลง LOW
        prow.value(0)
        time.sleep_us(50)  # หน่วงเล็กน้อยให้สัญญาณนิ่ง

        # เช็คทุก column
        for c, pcol in enumerate(cols):
            if pcol.value() == 0:  # ถ้ามีปุ่มกด (ต่อกราวด์)
                return key_map[r][c]

    return None

# ---------- แสดงเลข n (0–15) ด้วย LED 4 ดวง ----------
def show_number_on_leds(n):
    """
    แสดงเลข n เป็นฐานสอง 4 บิตบน LED:
    leds[0] = บิต b3 (MSB)
    leds[1] = บิต b2
    leds[2] = บิต b1
    leds[3] = บิต b0 (LSB)
    เช่น n = 5 -> 0101 -> LED = [0,1,0,1]
    """
    n &= 0xF  # เผื่อกันเกิน 4 บิต
    for i in range(4):
        bit = (n >> (3 - i)) & 1
        leds[i].value(bit)

# ---------- ลูปหลัก ----------
print("Ready... กดปุ่มบน keypad ได้เลย")

while True:
    k = scan_key()
    if k is not None:
        print("Key pressed:", k)

        if k in key_to_value:
            n = key_to_value[k]
            show_number_on_leds(n)
            print("Value:", n, "Binary: {:04b}".format(n))

        # รอจนปล่อยปุ่ม (กันเด้งซ้ำ)
        while scan_key() is not None:
            time.sleep_ms(20)

    time.sleep_ms(20)
