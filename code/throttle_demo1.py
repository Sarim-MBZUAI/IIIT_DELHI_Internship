import serial
import time

arduino = serial.Serial(port = 'COM3', timeout=0)
time.sleep(2)

while True:

    var = str(input())
    print ("You Entered :", var)
    arduino.write(str.encode(var))
    time.sleep(1)

    