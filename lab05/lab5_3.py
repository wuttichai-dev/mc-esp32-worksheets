from machine import I2C, Pin
from lcd_api import I2cLcd
import time

# --- 1. ตั้งค่า LCD ---
I2C_ADDR = 0x27
TOTAL_ROWS = 2
TOTAL_COLS = 16

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, TOTAL_ROWS, TOTAL_COLS)

btn_up = Pin(14, Pin.IN, Pin.PULL_UP)   
btn_down = Pin(12, Pin.IN, Pin.PULL_UP) 

count = 0

def update_display():
    lcd.move_to(0, 1) 
    lcd.putstr("Count: " + str(count) + "    ")


lcd.clear()
lcd.putstr("Counter System")
update_display() 

while True:
    if btn_up.value() == 0:  
        count += 1
        update_display()
        print("Count Up:", count) 
        time.sleep(0.5)      

    elif btn_down.value() == 0:
        count -= 1
        update_display()
        print("Count Down:", count)
        time.sleep(0.5)