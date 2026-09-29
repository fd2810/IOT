
# 1.Open Raspberry Pi Configuration
sudo raspi-config

Go to Interface Options → Camera then exit

# 2. Reboot
sudo reboot

# 3. Test the camera
libcamera-hello

# 4. Capture an image
libcamera-still -o image_name.jpg

# 5. Record a 10-second video
libcamera-vid -o video_name.h264 -t 10000








***Install module If libcamera-hello says "command not found"
sudo apt install -y rpicam-apps
(and replace libcamera commands with rpicam-apps)