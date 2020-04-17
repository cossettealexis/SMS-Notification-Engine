import shutil
import os

def CopyJsonFile():
    shutil.copy("./JsonFile\\SampleDatabase.json","./JsonRecycleBin")

def DeleteJson():
    os.remove("./JsonFile\\SampleDatabase.json")

def ResetFiles():
    shutil.copy("./JsonRecycleBin\\SampleDatabase.json","./JsonFile")
    os.remove("./JsonRecycleBin\\SampleDatabase.json")