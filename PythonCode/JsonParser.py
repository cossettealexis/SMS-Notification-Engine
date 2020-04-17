import JsonCopier
import time

def Run():
    print('Running Cossette Code')
    JsonCopier.CopyJsonFile()
    JsonCopier.DeleteJson()
    time.sleep(5)
    print("After Running the code")
    JsonCopier.ResetFiles()