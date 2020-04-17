import os
import time
import tkinter
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def on_created(event):
    global file
    file = event.src_path
    print("hey", event.src_path, "has been created")
    return str(file)        

def detect():
    global path
    path = "C:/Users/Cossette/Desktop/Arduino Controller/Phase 4"
    EventHandler = PatternMatchingEventHandler("*", "")
    EventHandler.on_created = on_created

    EventObserver = Observer()
    """EventObserver.schedule(
        EventHandler, "E:\\GitHub\\SMS_Notification_Engine\\JsonFile", False
    )"""
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
