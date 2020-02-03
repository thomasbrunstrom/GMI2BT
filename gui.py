from tkinter import *

class TKInterApp():
    def __init__(self):
        self.root = self.CreateMain()
        
        self.menu = self.CreateMenu()

        self.label = self.CreateLabel('Skriv något')

        self.textInput = self.CreateTextInput()

        self.listbox = self.CreateListbox()

        self.canvas = self.CreateCanvas()

        self.CreateButton('Klicka på mig', self.QuitApp)

        self.root.mainloop()

    def CreateMain(self):
        mainWindow = Tk()
        mainWindow.title('This is the main window')
        return mainWindow

    def CreateMenu(self):
        mm = Menu(self.root)
        mm2 = Menu(self.root)
        exitmenu = Menu(mm)
        mm.add_cascade(label = 'Menu', menu = exitmenu)
        mm.add_command(label = 'Töm canvas', command = self.ClearCanvas)
        exitmenu.add_command(label='Exit', command = self.QuitApp)
        #add menu to our main window
        self.root.config(menu=mm)

    def CreateButton(self, title, cmd):
        b = Button(self.root, text = title, command = cmd)
        b.grid(row=4, column=1, sticky=E)
    
    def CreateTextInput(self):
        e = Entry(self.root)
        e.bind('<KeyRelease>', self.TextCB)
        e.grid(row=1, column=1, sticky=EW)
        e.focus()
        return e

    def TextCB(self, ev):
        print(ev)
        print(self.textInput.get())
    
    def CreateLabel(self, text):
        lb = Label(self.root, text = text)
        lb.grid(row=1, column=0, sticky=W)

        return lb

    def CreateListbox(self):
        lb = Listbox(self.root)
        list = ['GIK299', 'GIK289', 'GIK297', 'GIK298']
        i = 0
        for l in list:
            lb.insert(i, l)
            i += 1

        lb.grid(row=2, column=0, columnspan=2, sticky=EW)
        return lb

    def CreateCanvas(self):
        c = Canvas(width = 200, height = 200, background = 'white')
        c.bind('<B1-Motion>', self.CanvasButtonDown)
        c.grid(row=3, column=0)
        return c
    
    def ClearCanvas(self):
        self.canvas.delete("all")

    def CanvasButtonDown(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, width=0, fill='black')

    def QuitApp(self):
        self.root.destroy()

mainWin = TKInterApp()