
import serial

def InitArduino():
    global ArduinoData
    ArduinoData = serial.Serial('/dev/ttyACM0', 9600)


InitArduino()