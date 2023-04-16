import tkinter
from tkinter import *
from graficos import graficos
from testes import captar_continentes


class NewWindowStart:

    def __init__(self):
        self.window = Tk()
        self.window.title("(Teste)Buscador de Informacoes de Paises")
        self.window.geometry("+300+160")
        self.window.minsize(height=200, width=200)
        self.window.resizable(False, False)

        self.country_select = None

        # Menu
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        # \menu
        self.menu_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menu", menu=self.menu_menu)

        # ___ em teste  __  ___________   __________________   _________
        self.menu_continente = Menu(self.menu, tearoff=0)
        self.menu_menu.add_cascade(label="Menu", menu=self.menu_continente)

        self.menu_continente.add_command(label="Paises de cada continente",
                                         command=self.executar_mostrar_paises)
        self.menu_continente.add_command(label="No de Paises por continente",
                                         command=self.executar_mostrar_numero_de_paises)
        # ____   ___  _______    _________   _____________  ________

        self.frame = Frame(self.window, bg="black")
        self.frame.pack()
        self.text = Text(self.window, font="Arial 9 bold", width=100, height=20, bg="grey90", bd=3)
        self.text.pack()

        self.sub_frame_left = Frame(self.frame, bg="grey90")
        self.sub_frame_left.pack(side="left")
        self.sub_frame_right = Frame(self.frame, bg="grey90")
        self.sub_frame_right.pack(side="right")

        self.label_text = Label(self.sub_frame_left, bg="grey90",
                                text="Teste",
                                font="Arial 7 bold")
        self.label_text.grid(row=0, column=0, columnspan=2)

        self.entry_place = Entry(self.sub_frame_left, font="arial 12", width=10, bd=3)
        self.entry_place.grid(row=1, column=0)

        self.button_search = Button(self.sub_frame_left, text="Search", font="Consolas 8 bold", bd=1,
                                    command=None)
        self.button_search.grid(row=1, column=1)

        self.list = Listbox(self.sub_frame_right, width=90, height=9, bd=2, bg="grey90")
        self.list.pack(fill="both")
        self.list.config(state=tkinter.DISABLED)

        self.window.mainloop()

    def executar_mostrar_paises(self):
        self.text.delete(1.0, "end")

        regioes = captar_continentes.mostrar_paises_de_cada_continente()
        text_memory = Text()

        text_memory.insert(1.0, f"{' '*10}   Paises de cada continente:")
        for iten in regioes:
            text_memory.insert("end", f"\n\n({iten})\n -  ")
            for i in regioes[iten]:
                text_memory.insert("end", f"{i},  ")
        self.text.insert("end", text_memory.get(1.0, "end"))

    def executar_mostrar_numero_de_paises(self):
        self.text.delete(1.0, "end")

        dicionario_temporario = captar_continentes.mostrar_numero_de_paises_de_cada_continente()

        # graficos.lines_graphic_ramp_up(dicionario_temporario, "Continentes", "No de paises", "Paises por Continentes")

        self.text.insert(1.0, f"   Quantidade de paises em cada continente:\n\n")
        for i in dicionario_temporario:
            self.text.insert("end", f"- {i}: {dicionario_temporario[i]}\n")


NewWindowStart()
