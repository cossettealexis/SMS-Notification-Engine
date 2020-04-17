import json

#import serial.tools.list_ports
#ports = list(serial.tools.list_ports.comports())


#Phase 1
#ArduinoData = serial.Serial('com4', 9600)
#Information = input()
#ArduinoData.write(str.encode(Information))

#Phase 2
#ArduinoData = serial.Serial('com4', 9600)

Module = 1
JsonFile = open("C:/Users/Cossette/Documents/GitHub/SMS_Notification_Engine/PythonCode/JsonFile/SampleDatabase.json")

CustomerInformation = json.load(JsonFile)
json.dumps(CustomerInformation)


for Customer in CustomerInformation['Username'] :
    print(Customer['fullname']+" "+ Customer['phone']+" "+Customer['Payment']+" I'M IN MODULE "+str(Module))
    #ArduinoData.write(str.encode(Customer['fullname']+" "+ Customer['phone']+" "+Customer['Payment']))"""
    Module+=1
    if Module == 11 :
        Module = 1






