import time
from Adafruit_PureIO.smbus import *

busnum = 1
bus = SMBus(busnum)

addr = 0x38
cmd = 0x001c
cmd_length = 2  #bytes
length = 4  #bytes
vals = [0x00,0x08,0x13,0x85]  # Should correxpond to vol 60
#bus.read_i2c_block_data(addr, cmd, cmd_length, length)
#time.sleep(0.1)
bus.write_i2c_block_data(addr, cmd, vals, cmd_length)
#time.sleep(0.1)
bus.read_i2c_block_data(addr, cmd, cmd_length, length)