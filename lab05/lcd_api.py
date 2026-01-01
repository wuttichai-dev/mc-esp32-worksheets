import time
from machine import I2C

class I2cLcd:
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.i2c.writeto(self.i2c_addr, bytes([0]))  
        time.sleep_ms(20)
        
        self.write_cmd(0x33)
        time.sleep_ms(5)
        self.write_cmd(0x32)
        time.sleep_ms(5)
        self.write_cmd(0x28)
        time.sleep_ms(5)
        self.write_cmd(0x0C)
        time.sleep_ms(5)
        self.write_cmd(0x06)
        time.sleep_ms(5)
        self.write_cmd(0x01)
        time.sleep_ms(5)

    def write_cmd(self, cmd):
        self._write_byte(cmd, 0)

    def write_data(self, data):
        self._write_byte(data, 1)

    def _write_byte(self, data, mode):

        high = mode | (data & 0xF0) | 0x08 
        low = mode | ((data << 4) & 0xF0) | 0x08
        
        self.i2c.writeto(self.i2c_addr, bytes([high, high | 0x04, high]))
        self.i2c.writeto(self.i2c_addr, bytes([low, low | 0x04, low]))

    def clear(self):
        self.write_cmd(0x01)
        time.sleep_ms(2)

    def putstr(self, string):
        for char in string:
            self.write_data(ord(char))

    def move_to(self, col, row):
        offsets = [0x00, 0x40, 0x14, 0x54]
        self.write_cmd(0x80 | (offsets[row] + col))