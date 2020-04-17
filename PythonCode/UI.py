import tkinter as Root
from tkinter import*

def SetUI():
    global Window
    global WindowCanvas
    global text
    Window = Root.Tk()
    text = Label(Window, text = "Scanning for new file..")
    text.pack()    
    Window.geometry("350x500")
    Window.title("SMS System")
    Window.resizable(False, False)
    Window.update_idletasks()
    Width = Window.winfo_width()
    Height = Window.winfo_height()
    X_Axis = (Window.winfo_screenwidth() // 2) - (Width // 2)
    Y_Axis = (Window.winfo_screenheight() // 2) - (Height // 2)
    Window.geometry('{}x{}+{}+{}'.format(Width, Height, X_Axis, Y_Axis))
    WindowCanvas = Canvas(Window)
    WindowFrame = Frame(WindowCanvas)
    #gif1 = PhotoImage(file ="C:/Users/Cossette/Downloads/Vanilla-1s-280px.gif")
    WindowCanvas.create_window(0, 0, anchor='nw', window=WindowFrame)
    #WindowCanvas.create_image(0, 0, image = gif1, anchor = 'nw')
    Window.mainloop()
    return text, WindowCanvas