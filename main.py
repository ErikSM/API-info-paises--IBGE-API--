from tkinter import *
import json
import requests


class Projecoes:

    def __init__(self):

        self.window = Tk()
        self.window.title("Busca de Informacoes Basicas de Paises")
        self.window.geometry("+300+160")
        self.window.minsize(height=200, width=200)
        self.window.resizable(0, 0)

        self.pais_desejado = None

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        self.menu_iniciar = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menu", menu=self.menu_iniciar)

        self.menu_iniciar.add_command(label="Indice de Paises", command=self.indice)

        self.frame = Frame(self.window, bg="grey90")
        self.frame.pack()

        self.texto = Text(self.window, font="Arial 9", width=100, height=20, bg="grey90", bd=3)
        self.texto.pack()

        self.sub_frame_equerdo = Frame(self.frame, bg="grey90")
        self.sub_frame_equerdo.pack(side="left")

        self.sub_frame_direito = Frame(self.frame, bg="grey90")
        self.sub_frame_direito.pack(side="right")

        self.label_text = Label(self.sub_frame_equerdo,
                                text="(Consulte o Menu acima) e\ndigite a sigla do pais desejado:", font="Arial 7 bold")
        self.label_text.grid(row=0, column=0, columnspan=2)

        self.text_entry = Entry(self.sub_frame_equerdo, font="arial 12", width=10, bd=3)
        self.text_entry.grid(row=1, column=0)

        self.button_search = Button(self.sub_frame_equerdo, text="Search", font="Consolas 8 bold", bd=1,
                                    command=self.search)
        self.button_search.grid(row=1, column=1)

        self.list = Listbox(self.sub_frame_direito, font="Consolas 8 bold", width=90, height=9, bd=2, bg="grey90")
        self.list.pack(fill="both")

        self.window.mainloop()

    def search(self):
        self.pais_desejado = self.text_entry.get().upper()

        try:
            request = requests.get(f""
                                   f"https://servicodados.ibge.gov.br/api/v1/paises/"
                                   f"{self.pais_desejado}"
                                   )

            dicionario = json.loads(request.text)

            self.texto.delete(1.0, END)
            self.list.delete(0, END)
            self.text_entry.delete(0, END)

            self.texto.config(bg="grey70")
            self.list.config(bg="grey70")
            for i in dicionario:
                self.list.insert(END, f'Pais: {i["nome"]["abreviado"]}')
                self.list.insert(END, f'Area: {i["area"]["total"]}{i["area"]["unidade"]["símbolo"]}')
                self.list.insert(END, f'Localizacao: {i["localizacao"]["regiao"]["nome"]}')
                self.list.insert(END, f'Lingua(s): {i["linguas"][0]["nome"]}')
                self.list.insert(END, f'Capital: {i["governo"]["capital"]["nome"]}')
                self.list.insert(END, f'Unidade monetaria: {i["unidades-monetarias"][0]["nome"]}')

                self.texto.insert(END, f'Historico: {i["historico"]}')
        except:
            self.list.insert(END, "   %##$  Informacoes nao encontradas ou Imprecisas   #$%& ")
            self.texto.insert(1.0, f"      #$%& ErRor #$%& ")

    def indice(self):

        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
        dicionario = json.loads(request.text)

        try:
            self.list.delete(0, END)
            self.list.insert(END, f"    {'-' * 1}  (( Indice de Paises )) {'-' * 1}   \n ")
        except:
            self.list.insert(END, f"    {'-' * 1}  (( Indice de Paises )) {'-' * 1}   \n ")

        self.texto.delete(1.0, END)
        self.text_entry.delete(0, END)
        self.texto.config(bg="grey90")
        self.list.config(bg="grey70")

        for i in dicionario:
            self.list.insert(END, f"Sigla: {i['id']['ISO-ALPHA-2']}{' ' * 15}"
                                  f"Estado: {i['nome']}{' ' * 2}\n")


Projecoes()
