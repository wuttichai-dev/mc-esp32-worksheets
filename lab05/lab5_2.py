from machine import I2C, Pin
from lcd_api import I2cLcd
import time

# --- การตั้งค่า (Setup) ---
I2C_ADDR = 0x27      # ตรวจสอบ Address ของจอ (บางรุ่น 0x3F)
TOTAL_ROWS = 2
TOTAL_COLS = 16

# เรียกใช้ I2C (ใช้ freq=100000 ตามที่เครื่องคุณเสถียร)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, TOTAL_ROWS, TOTAL_COLS)

# --- เริ่มทำงาน ---
lcd.clear()
lcd.putstr("Ready to Count!")
time.sleep(1)
lcd.clear()

while True:
    # Python ใช้ range(start, stop) โดยตัว stop จะไม่ถูกรวม
    # ดังนั้น range(1, 21) จะได้เลข 1, 2, 3 ... ถึง 20
    for number in range(1, 21):
        
        # บรรทัดที่ 1: แสดงข้อความหัวข้อ
        lcd.move_to(0, 0)        # คอลัมน์ 0, บรรทัด 0
        lcd.putstr("Counting: 1-20")
        
        # บรรทัดที่ 2: แสดงตัวเลข (จัดกึ่งกลาง)
        lcd.move_to(7, 1)        # ขยับไปตรงกลางๆ (คอลัมน์ 7, บรรทัด 1)
        
        # เทคนิคสำคัญ: แปลงเป็น string แล้วบวกช่องว่าง "  " ต่อท้าย
        # เพื่อลบเศษตัวเลขเก่า เวลาเปลี่ยนจากเลข 2 หลัก เป็นเลข 1 หลัก (ถ้ามี)
        lcd.putstr(str(number) + "  ")
        
        # หน่วงเวลา 0.5 วินาที (แก้ตรงนี้ถ้าอยากให้เร็ว/ช้า)
        time.sleep(0.5)

    # เมื่อนับครบ 20
    lcd.clear()
    lcd.move_to(4, 0)
    lcd.putstr("Success!")
    lcd.move_to(2, 1)
    lcd.putstr("Restarting...")
    
    time.sleep(2) # โชว์ข้อความจบ 2 วินาที แล้ววนกลับไปเริ่มใหม่
    lcd.clear()