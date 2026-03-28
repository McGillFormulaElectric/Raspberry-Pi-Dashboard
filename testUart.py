import serial
import time

ser = serial.Serial("/dev/ttyAMA5", 115200, timeout=1)

print('Listening...')


while True:
	#ser.write(b'A')
	if ser.in_waiting > 0:
		print('w0aiting...')
		b = ser.read(1)
		if b: 
			print("RX byte:", b[0], b.hex())
			print(b)
