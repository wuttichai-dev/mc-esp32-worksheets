from machine import I2C, Pin
from lcd_api import I2cLcd  # เรียกใช้ Library ที่เพิ่งสร้าง
import time

# ตั้งค่า I2C Address (0x27 คือค่ามาตรฐาน, บางรุ่นอาจเป็น 0x3F)
I2C_ADDR = 0x27
TOTAL_ROWS = 2
TOTAL_COLS = 16

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=10000)

try:
    lcd = I2cLcd(i2c, I2C_ADDR, TOTAL_ROWS, TOTAL_COLS)
    
    lcd.clear()            
    lcd.putstr("Hello RMUTK !!!")
    
    lcd.move_to(0, 1)      
    lcd.putstr("MicroPython LCD")
    
    print("LCD Initialized Successfully")

except OSError:
    print("Error: LCD not found! Check wiring or I2C Address.")


