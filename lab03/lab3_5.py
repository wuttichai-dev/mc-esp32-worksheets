from machine import Pin
import time

# ---------- ตั้งค่า LED ----------
leds = [Pin(p, Pin.OUT) for p in (16, 17, 18, 19)]

def leds_all(on_off):
    """on_off = 1 ติดทุกดวง, 0 ดับทุกดวง"""
    for led in leds:
        led.value(on_off)

def blink_error(times=3):
    """กระพริบ LED บอกว่ารหัสผิด"""
    for _ in range(times):
        leds_all(0)
        time.sleep_ms(200)
        leds_all(1)
        time.sleep_ms(200)
    leds_all(0)

leds_all(0)  # เริ่มต้น ปิดไฟก่อน

# ---------- ตั้งค่า Keypad ----------
rows = [Pin(p, Pin.OUT) for p in (21, 22, 23, 25)]
cols = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (26, 27, 32, 33)]

# แผนผังปุ่มบน keypad 4x4
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D'],
]

# ---------- ฟังก์ชันอ่านปุ่ม ----------
def scan_key():
    """ถ้ามีปุ่มกด คืนค่าเป็นตัวอักษรของปุ่ม, ถ้าไม่กด คืนค่า None"""
    for r in range(4):
        # ให้ทุก row เป็น 1 ก่อน
        for i in range(4):
            rows[i].value(1)

        # ดึง row ที่กำลังตรวจให้เป็น 0
        rows[r].value(0)
        time.sleep_us(50)

        # ตรวจทุก column
        for c in range(4):
            if cols[c].value() == 0:   # มีปุ่มถูกกด (ต่อกราวด์)
                return keys[r][c]

    return None

# ---------- รหัสผ่าน ----------
PASSWORD = ['1', '2', '3', '4']
input_code = []   # เอาไว้เก็บปุ่มที่กด

print("Ready... ใส่รหัส 4 หลักด้วย keypad")

# ---------- ลูปหลัก ----------
while True:
    k = scan_key()

    if k is not None:
        print("กดปุ่ม:", k)

        # เก็บตัวที่กด (จะกดอะไรก็เก็บไว้ก่อน ทั้งตัวเลขและตัวอักษร)
        input_code.append(k)
        print("input_code =", input_code)

        # รอจนปล่อยปุ่ม (กันไม่ให้กดครั้งเดียวแต่โดนอ่านหลายรอบ)
        while scan_key() is not None:
            time.sleep_ms(20)

        # ถ้ากดครบ 4 ตัวแล้ว
        if len(input_code) == 4:
            if input_code == PASSWORD:
                print("รหัสถูกต้อง!")
                leds_all(1)          # แสดง 1111
                time.sleep(1)        # ติดค้าง 1 วินาที
                leds_all(0)
            else:
                print("รหัสผิด!")
                blink_error(3)       # กระพริบเตือน 3 รอบ

            # เคลียร์เพื่อรอรับรหัสใหม่
            input_code = []

    time.sleep_ms(20)
