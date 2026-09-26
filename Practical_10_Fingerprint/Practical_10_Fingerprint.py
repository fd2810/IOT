import time
import sys
from pyfingerprint.pyfingerprint import PyFingerprint

print("Initializing fingerprint sensor...")

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if not f.verifyPassword():
        raise ValueError("Fingerprint sensor password is incorrect.")
    print("Sensor initialized successfully.")
except Exception as e:
    print(f"Initialization failed: {e}")
    sys.exit(1)


def enrollFinger():
    print("Enrolling Finger...")
    print("Place finger on sensor...")
    while not f.readImage():
        time.sleep(0.1)

    f.convertImage(0x01)
    result = f.searchTemplate()
    positionNumber = result[0]

    if positionNumber >= 0:
        print(f"Template already exists at position #{positionNumber}")
        time.sleep(2)
        return

    print("Remove finger...")
    while f.readImage():
        time.sleep(0.1)

    print("Place the same finger again...")
    while not f.readImage():
        time.sleep(0.1)

    f.convertImage(0x02)

    if f.compareCharacteristics() == 0:
        print("Fingers do not match.")
        time.sleep(2)
        return

    f.createTemplate()
    positionNumber = f.storeTemplate()
    print("Finger enrolled successfully.")
    print(f"Stored at position: {positionNumber}")
    time.sleep(2)


def searchFinger():
    try:
        print("Waiting for finger (place finger now)...")
        while not f.readImage():
            time.sleep(0.1)

        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print("No match found.")
            time.sleep(2)
            return False
        else:
            print(f"Found template at position #{positionNumber}")
            time.sleep(2)
            return True

    except Exception as e:
        print(f"Search failed: {e}")
        return False


def deleteFinger():
    try:
        print("Waiting for finger to delete...")
        while not f.readImage():
            time.sleep(0.1)

        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print("No match found.")
            time.sleep(2)
            return False
        else:
            if f.deleteTemplate(positionNumber):
                print(f"Template at position #{positionNumber} deleted successfully.")
                time.sleep(2)
                return True

    except Exception as e:
        print(f"Delete failed: {e}")
        return False


time.sleep(1)
print("System Ready.")

while True:
    print("\nSelect an option:\n1. Enroll\n2. Search\n3. Delete\n4. Exit")
    choice = input("Enter choice (1-4): ").strip()

    if choice == '1':
        enrollFinger()
    elif choice == '2':
        searchFinger()
    elif choice == '3':
        deleteFinger()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Pin 1: VCC (Red wire)    -> Connect to USB-TTL: 5V / VCC
# Pin 2: GND (Black wire)  -> Connect to USB-TTL: GND
# Pin 3: TX  (Yellow wire) -> Connect to USB-TTL: RX
# Pin 4: RX  (White wire)  -> Connect to USB-TTL: TX



