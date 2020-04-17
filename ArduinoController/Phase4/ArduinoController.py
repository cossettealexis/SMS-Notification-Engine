#!user/bin/python3.5
import threading
#import tkinter
#from tkinter import*
#from tkinter import messagebox
import time
import json
import JsonDetector
import serial
import UI
import ArduinoMonitor

def RunAutomaticMessaging():
    print("Application is Starting")
    ArduinoMonitor.InitArduino()
    Counter = 1
    Thread_One = threading.Thread(target = UI.SetUI)
    Thread_One.start()
    JsonDetector.detect()

    # file = str(JsonDetector.file)   
    # UI.text.pack_forget()
    
    # #ArduinoData = serial.Serial("com19", 9600)
    # ArduinoData = serial.Serial('/dev/tty1', 9600)
    # JsonFile = open(file)
    # CustomerInformation = json.load(JsonFile)
    # json.dumps(CustomerInformation)

    # for Customer in CustomerInformation["Username"]:
    #     ArduinoData.write(
    #                 str.encode(
    #                     Customer["fullname"]
    #                     + " "
    #                     + Customer["phone"]
    #                     + " "
    #                     + Customer["Payment"]
    #                 )
    #             )
    #     print(
    #         str.encode(
    #             Customer["fullname"]
    #             + " "
    #             + Customer["phone"]
    #             + " "
    #             + Customer["Payment"]
    #         )
    #     )
    #     if Counter % 27 == 0:
    #                 for  Widgets in UI.WindowCanvas.winfo_children():
    #                     if Widgets != 'Window':
    #                         Widgets.pack_forget()
    #     else:
    #         time.sleep(10)  
    #         Output = Entry(UI.WindowCanvas)
    #         Output.pack(fill = X)
    #         Notification = str("Message to "+ Customer["fullname"] + " "+Customer["phone"]+ " was successfully sent!") 
    #         Output.insert(0, Notification)
    #         UI.WindowCanvas.update_idletasks()
    #         UI.WindowCanvas.update()
    #         UI.WindowCanvas.pack(fill='both', expand=True, side='left')

    # #Thread_One.join()
           
RunAutomaticMessaging()