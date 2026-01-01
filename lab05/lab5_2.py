from machine import I2C, Pin
from lcd_api import I2cLcd
import time

I2C_ADDR = 0x27      
TOTAL_ROWS = 2
TOTAL_COLS = 16

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, TOTAL_ROWS, TOTAL_COLS)

lcd.clear()
lcd.putstr("Ready to Count!")
time.sleep(1)
lcd.clear()

while True:
    for number in range(1, 21):
        
        lcd.move_to(0, 0)        
        lcd.putstr("Counting: 1-20")
        
        lcd.move_to(7, 1)    
        
        lcd.putstr(str(number) + "  ")
        
        time.sleep(0.5)

    lcd.clear()
    lcd.move_to(4, 0)
    lcd.putstr("Success!")
    lcd.move_to(2, 1)
    lcd.putstr("Restarting...")
    
    time.sleep(2) 
    lcd.clear()