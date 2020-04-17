#!user/bin/python3.5
import threading
import tkinter
from tkinter import*
from tkinter import messagebox
import time
import json
import JsonDetector
import serial
import UI
import ArduinoMonitor
#import ArduinoController


def RunAutomaticMessaging():
    Counter = 1
    file = str(JsonDetector.file)   
    UI.text.pack_forget()
    
    JsonFile = open(file)
    CustomerInformation = json.load(JsonFile)
    json.dumps(CustomerInformation)

    for Customer in CustomerInformation["Username"]:
        ArduinoMonitor.ArduinoData.write(
                    str.encode(
                        Customer["fullname"]
                        + " "
                        + Customer["phone"]
                        + " "
                        + Customer["Payment"]
                    )
                )
        time.sleep(10)
        print(
            str.encode(
                Customer["fullname"]
                + " "
                + Customer["phone"]
                + " "
                + Customer["Payment"]
            )
        )
        if Counter % 27 == 0:
                    for  Widgets in UI.WindowCanvas.winfo_children():
                        if Widgets != 'Window':
                            Widgets.pack_forget()
        else:
            time.sleep(10)  
            Output = Entry(UI.WindowCanvas)
            Output.pack(fill = X)
            Notification = str("Message to "+ Customer["fullname"] + " "+Customer["phone"]+ " was successfully sent!") 
            Output.insert(0, Notification)
            UI.WindowCanvas.update_idletasks()
            UI.WindowCanvas.update()
            UI.WindowCanvas.pack(fill='both', expand=True, side='left')

    #Thread_One.join()
           
#ArduinoController.RunAutomaticMessaging()