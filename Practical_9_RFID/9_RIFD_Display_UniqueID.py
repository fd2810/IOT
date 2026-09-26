import subprocess
import time
NAME = "Upasana"   # Put your name here
last_uid = None
try:
    while True:
        output = subprocess.getoutput("nfc-list")
        if "UID" in output:
            for line in output.splitlines():
                if "UID" in line:
                    uid = line.split(":")[1].strip().replace(" ", "")
                    if uid != last_uid:
                        print(f"{NAME}: {uid}")
                        last_uid = uid
                    break
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped")

# Command 1: sudo raspi-config
#             -> Enable I2C

# Command 2: sudo reboot

# Command 3: pip3 install adafruit-circuitpython-pn532 --break-system-packages

# Command 4: sudo apt install -y libnfc-bin libnfc-dev libusb-dev libpcsclite-dev i2c-tools

# Command 5: sudo nano /etc/nfc/libnfc.conf

# Command 6: i2cdetect -y 1

# Command 7: nfc-list
