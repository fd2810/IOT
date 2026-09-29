GND (Ground): RPI Pin 14 (Raspberry Function: GND)
VCC (+5V Power): RPI Pin 4 (Raspberry Function: 5V)
DI0 (Data In): RPI Pin 18 (Raspberry Function: GPIO 24)
CLK (Clock): RPI Pin 16 (Raspberry Function: GPIO 23) 

commands:-

sudo raspi-config
# Enable I2C
pip install board --break-system-packages
sudo pip install drawnow --break-system-packages
sudo apt-get install -y i2c-tools python3-smbus
python3 -m pip install --upgrade --no-cache-dir adafruit-blinka adafruit-circuitpython-busdevice adafruit-circuitpython-ads1x15 --break-system-packages



