from tkinter import *
from graficos import graficos

class Window:

    def __init__(self):
        self.window = Tk()
        self.window.title("Janela teste")
        self.window.geometry("+300+160")
        self.window.minsize(height=200, width=200)
        self.window.resizable(0, 0)

        self.imagem = self.executar()

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.menu_start = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menu", menu=self.menu_start)
        self.menu_start.add_command(label="teste", command=None)

        self.label = Label(self.window, image=self.imagem)

        self.window.mainloop()

    def executar(self):
        dict = {'haha': 1, "xx": 2}
        graficos.lines_graphic_ramp_up(dict)

Window()