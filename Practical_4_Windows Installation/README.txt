VCC: Pin 2
GND: Pin 6   
Tx: Pin 10   

1. create and activate virtual environment
2. Enter the commands one by one:-
	dtparam=spi=on
	dtoverlay=pi3-disable-dt
	core_freq=250
	enable_uart=1
	force_turbo=1
	sudo systemctl stop serial-getty@ttyS0.service
	sudo systemctl disable serial-getty@ttyS0.service
	sudo systemctl enable serial-getty@ttyAMA0.service
3. sudo apt-get install minicom
4. pip install pynmea2 --break-system-packages
5. sudo cat /dev/tty/S0
