import os
import time
#import tkinter
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import Test11


def on_created(event):
    time.sleep(10)
    global file
    file = event.src_path
    print("hey", event.src_path, "has been created")
    Test11.RunAutomaticMessaging()
    return str(file)        

def detect():
    global path
    path = "/home/pi/Desktop/SMS_Receive"
    EventHandler = PatternMatchingEventHandler("*", "")
    EventHandler.on_created = on_created

    EventObserver = Observer()
    # """EventObserver.schedule(
    #     EventHandler, "E:\\GitHub\\SMS_Notification_Engine\\JsonFile", False
    # )"""
    EventObserver.schedule(
        EventHandler, path, False
    )
    EventObserver.start()
    try:
        while True:
            time.sleep(1)
            

    except KeyboardInterrupt:
        EventObserver.stop()
        EventObserver.join()
