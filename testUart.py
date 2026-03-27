import serial
import time

ser = serial.Serial("/dev/ttyAMA5", 9600, timeout=1)

print("Listening...")


while True:
	if ser.in_waiting > 0:
		b = ser.read(1)
		if b: 
			print("RX byte:", b[0], b.hex())
			print(b)
