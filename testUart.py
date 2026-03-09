import serial

ser = serial.Serial("/dev/ttyAMA0",9600, timeout=0)

print('Listening...')

while True:
	ser.write(b'A')
	if ser.in_waiting > 0:
		print('w0aiting...')
		b = ser.read(1)
		print("RX byte:", b[0])

