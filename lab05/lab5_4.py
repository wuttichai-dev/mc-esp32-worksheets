from machine import Pin, I2C
from lcd_api import I2cLcd
import time

PASSWORD = "1234"

I2C_ADDR = 0x27
TOTAL_ROWS = 2
TOTAL_COLS = 16

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
try:
    lcd = I2cLcd(i2c, I2C_ADDR, TOTAL_ROWS, TOTAL_COLS)
except:
    print("LCD Error: Check wiring or I2C Address")

KEY_MAP = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

ROW_PINS = [13, 12, 14, 27]
COL_PINS = [26, 25, 33, 32]

rows = [Pin(pin, Pin.OUT) for pin in ROW_PINS]
cols = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in COL_PINS]

def read_keypad():
    for r in range(4):
        rows[r].value(1) 
        for c in range(4):
            if cols[c].value() == 1: 
                while cols[c].value() == 1: 
                    time.sleep(0.01)
                rows[r].value(0)
                return KEY_MAP[r][c] 
        rows[r].value(0) 
    return None

def main():
    input_buffer = ""
    
    lcd.clear()
    lcd.putstr("Enter Pass:")
    lcd.move_to(0, 1)
    
    while True:
        key = read_keypad()
        
        if key: 
            print(f"Key pressed: {key}")
            
            if key == '*':
                input_buffer = ""
                lcd.clear()
                lcd.putstr("Cleared")
                time.sleep(1)
                lcd.clear()
                lcd.putstr("Enter Pass:")
                lcd.move_to(0, 1)
                continue
            
            input_buffer += key
            lcd.putstr("*") 
            
            if len(input_buffer) == 4:
                time.sleep(0.5) 
                lcd.clear()
                
                if input_buffer == PASSWORD:
                    lcd.putstr("Correct Password")
                    print("Result: Correct")
                else:
                    lcd.putstr("Wrong Password")
                    print("Result: Wrong")
                
                time.sleep(2)
                
                input_buffer = ""
                lcd.clear()
                lcd.putstr("Enter Pass:")
                lcd.move_to(0, 1)

try:
    main()
except KeyboardInterrupt:
    print("Stopped")