import tkinter
from tkinter import *
import json
import requests


class AppStart:

    def __init__(self):

        self.window = Tk()
        self.window.title("Busca de Informacoes Basicas de Paises")
        self.window.geometry("+300+160")
        self.window.minsize(height=200, width=200)
        self.window.resizable(0, 0)

        self.country_select = None

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.menu_start = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menu", menu=self.menu_start)
        self.menu_start.add_command(label="Indice de Paises", command=self.index)

        self.frame = Frame(self.window, bg="grey90")
        self.frame.pack()
        self.text = Text(self.window, font="Arial 9 bold", width=100, height=20, bg="grey90", bd=3)
        self.text.pack()

        self.sub_frame_left = Frame(self.frame, bg="grey90")
        self.sub_frame_left.pack(side="left")
        self.sub_frame_right = Frame(self.frame, bg="grey90")
        self.sub_frame_right.pack(side="right")

        self.label_text = Label(self.sub_frame_left, bg="grey90",
                                text="(Consulte o Menu acima) e\ndigite a sigla do pais desejado:", font="Arial 7 bold")
        self.label_text.grid(row=0, column=0, columnspan=2)

        self.entry_place = Entry(self.sub_frame_left, font="arial 12", width=10, bd=3)
        self.entry_place.grid(row=1, column=0)

        self.button_search = Button(self.sub_frame_left, text="Search", font="Consolas 8 bold", bd=1,
                                    command=self.search)
        self.button_search.grid(row=1, column=1)

        self.list = Listbox(self.sub_frame_right, width=90, height=9, bd=2, bg="grey90")
        self.list.pack(fill="both")
        self.list.config(state=tkinter.DISABLED)

        self.window.mainloop()

    def search(self):
        self.list.config(state=tkinter.NORMAL)

        self.country_select = self.entry_place.get().upper()

        try:
            request = requests.get(f""
                                   f"https://servicodados.ibge.gov.br/api/v1/paises/"
                                   f"{self.country_select}"
                                   )

            dict_of_search = json.loads(request.text)

            self.text.delete(1.0, END)
            self.list.delete(0, END)
            self.entry_place.delete(0, END)

            self.text.config(bg="grey70")
            self.list.config(bg="grey70")
            for item in dict_of_search:
                self.list.insert(END, f'Pais: {item["nome"]["abreviado"]}')
                self.list.insert(END, f'Area: {item["area"]["total"]}{item["area"]["unidade"]["símbolo"]}')
                self.list.insert(END, f'Localizacao: {item["localizacao"]["regiao"]["nome"]}')
                self.list.insert(END, f'Lingua(s): {item["linguas"][0]["nome"]}')
                self.list.insert(END, f'Capital: {item["governo"]["capital"]["nome"]}')
                self.list.insert(END, f'Unidade monetaria: {item["unidades-monetarias"][0]["nome"]}')

                self.text.insert(END, f'Historico: {item["historico"]}')
        except Exception as ex:
            self.list.insert(END, "   %##$  Informacoes nao encontradas ou Imprecisas   #$%& ")
            self.text.insert(1.0, f"{ex}\n\n      #$%& ErRor #$%& ")

    def index(self):

        self.list.config(state=tkinter.NORMAL)
        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
        dict_of_indexes = json.loads(request.text)

        self.list.insert(END, "...")
        self.list.delete(0, END)
        self.list.insert(END, f"    {'-' * 1}  (( Indice de Paises )) {'-' * 1}   \n ")

        self.text.insert(END, "...")
        self.text.delete(1.0, END)

        self.entry_place.delete(0, END)
        self.text.config(bg="grey90")
        self.list.config(bg="grey70")

        for country in dict_of_indexes:
            self.list.insert(END, f"Sigla: {country['id']['ISO-ALPHA-2']}{' ' * 15}"
                                  f"Estado: {country['nome']}{' ' * 2}\n")

        self.list.config(state=tkinter.DISABLED)


AppStart()
