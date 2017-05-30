from Adafruit_PureIO.smbus import *

busnum = 1
bus = SMBus(busnum)

addr = 0x38
cmd = 0x001c
cmd_length = 2  #bytes
length = 4  #bytes
bus.read_i2c_block_data(addr, cmd, cmd_length, length)
