import machine
import utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

# linear interpolation for battery percentage approximation
# Of course not accurate since batteries are non-linear systems.
def battery_percent(v_in):
    BATT_MIN=7.2
    BATT_MAX=9
    if v_in <= BATT_MIN:
        return 0
    elif v_in >= BATT_MAX:
        return 100
    else:
        percentage=100*((v_in-BATT_MIN)/(BATT_MAX-BATT_MIN))
        return int(percentage)

WIDTH  = 128                                            # oled display width (X)
HEIGHT = 64                                             # oled display height (Y)

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)     # Init I2C using pins GP21 & GP20 (Channel I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c, 0x3D)            # Init oled display

adc=machine.ADC(26)

oled.fill(0)
oled.text("Rodrigo",73,0)
oled.text("Espinoza",65,10)
oled.text("Battery USC",20,30) # Usable System Capacity

while True:
    raw_adc=adc.read_u16()
    v_out=raw_adc*3.23/65536
    v_in=v_out*59/20 #calculated using actual resistor values
    print("*************************")
    print("ADC reading:", raw_adc)
    print("Voltage output:"+str(v_out)+"V")
    print("Voltage input:"+str(v_in)+"V")
    print("Battery Percentage:"+str(battery_percent(v_in))+"%")
    oled.fill_rect(64,40,32,8,0)
    oled.text(str(battery_percent(v_in))+"%",64,40)
    oled.show()
    utime.sleep(1)
