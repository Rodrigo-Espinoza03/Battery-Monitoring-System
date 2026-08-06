# Battery-Monitoring-System
Monitors the voltage supplied to a 7.2V electronic device.

# Software
This code converts an analog value from the midpoint of a voltage divider to measure the voltage output.
Once voltage output is found through 16-bit raw data, a mathematical algorithm with measured voltage reference
and actual resistor values are used to calculate the voltage input. 

A linear interpolation is used to approximate the power supply's usable system capacity. Voltage percentage is 
displayed onto Adafruit's SSD1306 OLED display using I2C protocol.

# Hardware
A voltage divider is used to step down the battery voltage to safely connect to the pico's adc pin. This is to 
ensure that the voltage level remains under the adc reference voltage threshold. A capacitor is implemented to
create a low-pass filter to attenuate high frequencies. 

The wiring for the oled is connected to the pico's gpio pin configured for the hardware I2C peripheral.

Nominal resistor values: R1=2k ohms, R2=1k ohms. Actual resistance determined using digital multimeter.
Capacitor value: 100nF

# Components Used
* **Board:** Raspberry Pi Pico H 
* **IC:** Adafruit SSD1306 OLED
* **Components:** 1 capacitor & 2 resistors
* **Power Supply:** 3800mAH 7.2V GEILIENERGY NIMH Battery
