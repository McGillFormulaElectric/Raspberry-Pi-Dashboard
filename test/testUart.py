import serial
import time

ser = serial.Serial("/dev/ttyAMA5", 115200, timeout=5)

print('Listening...')


while True:
	#ser.write(b'A')
	if ser.in_waiting >= 3:
		print('w0aiting...')
		b = ser.read(3)
		if b: 
			print("RX byte:",list(b))
			#print(b)
