from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ArduinoController.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "SMS System",
    options = options,
    version = "1.0",
    description = 'SMS System',
    executables = executables
)