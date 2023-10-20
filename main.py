import machine
import time
# Initialize SoftI2C interface
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000)

def read_gas_flow(): #read in SLPM
    msb, lsb = i2c.readfrom(0x07, 2)
    #print(msb, lsb)
    return ((msb << 8) + lsb) / 1000.0

# Continuously read and print flow rate with a 10ms delay
while True:
    #read_gas_flow()
    print(read_gas_flow())
    time.sleep_ms(10)