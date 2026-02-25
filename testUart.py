import serial

ser = serial.Serial("/dev/serial0", 115200, timeout=0)

print("Listening...")

while True:
	if ser.in_waiting > 0:
		b = ser.read(1)
		if b: 
			print("RX byte:", b[0], b.hex())
