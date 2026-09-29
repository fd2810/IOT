# IOT Practical

This repository contains Python programs and practicals for **IoT using Raspberry Pi**.

## Files

* `LED.py` – LED blinking using Raspberry Pi GPIO.
* `telegram_led.py` – Controls an LED using a Telegram bot.
* `digital_clock.py` – Displays the current time using a TM1637 4-digit display.
* `oscilloscope.py` – Software oscilloscope using ADS1115 ADC.
* `fingerprint.py` – Fingerprint enrollment, searching, and deletion using a fingerprint sensor.

> File names may be different depending on the practical. The above descriptions explain the purpose of each program.

---

# Python Virtual Environment

A virtual environment is used to install Python packages separately for this project without affecting the system Python installation.

## 1. Create Virtual Environment

Open the Raspberry Pi terminal and go to the project folder:

```bash
cd ~/IOT
```

Create a virtual environment:

```bash
python3 -m venv venv
```

If `venv` is not installed:

```bash
sudo apt install python3-venv
```

Then create it again:

```bash
python3 -m venv venv
```

## 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

After activation, the terminal will show something similar to:

```text
(venv) pi@raspberrypi:~/IOT $
```

Now Python packages installed using `pip` will be installed inside this virtual environment.

## 3. Install Required Packages

After activating the virtual environment:

```bash
pip install RPi.GPIO
pip install pyserial
pip install pyfingerprint
```

For the ADS1115 practical:

```bash
pip install adafruit-blinka
pip install adafruit-circuitpython-ads1x15
pip install numpy
pip install matplotlib
```

For the Telegram bot practical:

```bash
pip install telepot
```

For the TM1637 practical:

```bash
pip install tm1637
```

## 4. Check Installed Packages

```bash
pip list
```

## 5. Deactivate Virtual Environment

When finished working:

```bash
deactivate
```

The `(venv)` text will disappear from the terminal.

## 6. Activate It Again Later

You do not need to create the environment again.

Go to the project folder:

```bash
cd ~/IOT
```

Then activate it:

```bash
source venv/bin/activate
```

## Important

The `venv` folder should normally **not be uploaded to GitHub**. Add it to `.gitignore`:

```text
venv/
__pycache__/
*.pyc
```

Then Git will ignore the virtual environment and Python cache files.
