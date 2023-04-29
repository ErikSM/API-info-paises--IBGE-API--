import tkinter
from tkinter import *
import json
import requests

from actions import capture_indicators, capture_continents


def start(window=None):
    if window is not None:
        window.destroy()
    AppStart()


class AppStart:

    def __init__(self):

        self.country_select = None

        self.country_open = None
        self.sigla_of_open_country = None

        self.window = Tk()
        self.window.title("Busca de Informacoes Basicas de Paises")
        self.window.geometry("+400+100")
        self.window.minsize(height=200, width=200)
        self.window.resizable(False, False)

        # / Menus
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        # // inicio
        self.menu.add_command(label="Tela inicial", command=lambda: start(self.window))

        # // incides
        self.menu_indices = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Indices", menu=self.menu_indices)
        self.menu_indices.add_command(label="Indice de Paises", command=self.index)

        # // continentes(em desenvolvimento)
        self.menu_continentes = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Continentes", menu=self.menu_continentes)
        self.menu_continentes.add_command(label="Sobre continentes", command=self.abrir_continentes)

        self.frame = Frame(self.window, bg="grey90")
        self.frame.pack()
        self.text = Text(self.window, font="Arial 9 bold", width=100, height=20, bg="grey90", bd=3)
        self.text.pack()

        self.sub_frame_left = Frame(self.frame, bg="grey90")
        self.sub_frame_left.pack(side="left")
        self.sub_frame_right = Frame(self.frame, bg="grey90")
        self.sub_frame_right.pack(side="right")

        self.label_of_search = None
        self.entry_of_search = None
        self.button_search = None
        self.label_of_list = None
        self.initial_settings()

        self.button_return = None

        self.list = Listbox(self.sub_frame_right, width=90, height=9, bd=2, bg="grey90")
        self.list.pack(fill="both")
        self.list.config(state=tkinter.DISABLED)

        self.window.mainloop()

    def initial_settings(self):
        self.label_of_search = Label(self.sub_frame_left, font="Arial 7 bold", bg="grey90")
        self.label_of_search.configure(text="(Consulte o Menu indice acima) e\ndigite a sigla do pais desejado:")
        self.label_of_search.grid(row=0, column=0, columnspan=2)

        self.entry_of_search = Entry(self.sub_frame_left, font="arial 12", width=10, bd=3)
        self.entry_of_search.grid(row=1, column=0)

        self.button_search = Button(self.sub_frame_left)
        self.button_search.configure(font="Consolas 8 bold", text="Busca", bd=1, command=self.search)
        self.button_search.grid(row=1, column=1)

        self.label_of_list = Label(self.sub_frame_right)
        self.label_of_list.configure(text="-----------   ----------- :", bg="grey90")
        self.label_of_list.pack()

    def back_to_search_settings(self):
        self.button_return.destroy()
        self.initial_settings()
        self.entry_of_search.insert(0, self.country_select)
        self.search()

    def search(self):
        self.list.config(state=tkinter.NORMAL)

        self.country_select = self.entry_of_search.get().upper()

        if len(self.country_select) == 0:
            self.text.delete(1.0, END)
            self.list.delete(0, END)

            self.list.insert(END, f"   {'X' * 10} ")
            self.list.insert(END, "   %##$  Informacoes nao encontradas ou Imprecisas   #$%& ")
            self.text.insert(1.0, f"\n\n{'X' * 10}\n\n      #$%& ErRor #$%& ")
        else:
            request = requests.get(f""
                                   f"https://servicodados.ibge.gov.br/api/v1/paises/"
                                   f"{self.country_select}"
                                   )

            dict_of_search = json.loads(request.text)

            self.text.delete(1.0, END)
            self.list.delete(0, END)
            self.entry_of_search.delete(0, END)

            self.text.config(bg="grey70")
            self.list.config(bg="grey70")

            self.label_of_list.config(text=" Informacoes basicas:")
            for item in dict_of_search:
                self.list.insert(END, f'Pais: {item["nome"]["abreviado"]}')
                self.list.insert(END, f'Area: {item["area"]["total"]}{item["area"]["unidade"]["símbolo"]}')
                self.list.insert(END, f'Localizacao: {item["localizacao"]["regiao"]["nome"]}')
                self.list.insert(END, f'Lingua(s): {item["linguas"][0]["nome"]}')
                self.list.insert(END, f'Capital: {item["governo"]["capital"]["nome"]}')
                self.list.insert(END, f'Unidade monetaria: {item["unidades-monetarias"][0]["nome"]}')

                self.text.insert(END, f'Historico: {item["historico"]}')

                self.country_open = item["nome"]["abreviado"]
                self.country_open = self.country_open.lower()

            self.sigla_of_open_country = self.country_select

            self.button_search.config(text=f"<Informacoes avancadas>")
            self.button_search.configure(command=self.advanced_information_about_country)
            self.label_of_search.config(text=f"Clique para outros indicadores\nsobre:({self.country_open.title()})")
            self.entry_of_search.destroy()

    def index(self):
        self.list.config(state=tkinter.NORMAL)
        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
        dict_of_indexes = json.loads(request.text)

        self.label_of_list.config(text=" Confira abaixo as siglas dos paises:")

        self.list.insert(END, "...")
        self.list.delete(0, END)
        self.list.insert(END, f"    {'-' * 1}  (( Indice de Paises )) {'-' * 1}   \n ")

        self.text.insert(END, "...")
        self.text.delete(1.0, END)

        self.entry_of_search.delete(0, END)
        self.text.config(bg="grey90")
        self.list.config(bg="grey70")

        for country in dict_of_indexes:
            self.list.insert(END, f"Sigla: {country['id']['ISO-ALPHA-2']}{' ' * 15}"
                                  f"Estado: {country['nome']}{' ' * 2}\n")

        self.list.config(state=tkinter.DISABLED)

    def advanced_information_about_country(self):
        all_indicators = capture_indicators.show_indicators_id()
        country_indicators = capture_indicators.show_all_indicators_of_selected_country(self.sigla_of_open_country)

        self.label_of_list.config(text=f"Informacoes detalhadas sobre: ({self.country_open.title()}):")
        self.label_of_search.config(text="Busque pelo item selecionado:")
        self.button_search.config(text=f"Especificar indicador")
        self.button_search.configure(command=self.show_selected_indicator)

        self.list.config(state=tkinter.NORMAL)

        self.list.delete(0, END)
        self.text.delete(1.0, END)

        for i in all_indicators:
            indicator = i
            indicator_code = all_indicators[i]
            self.list.insert(END, f"{indicator_code}:  {indicator}")

        for i in country_indicators:
            indicator = f"({i['id']}){i['indicador']}: {i['series'][0]['pais']}"
            information = f"{i['series'][0]['serie']}"
            self.text.insert(END, f"{indicator}\n")
            self.text.insert(END, f"{information}\n\n")

    def show_selected_indicator(self):
        country = self.sigla_of_open_country
        indicator = self.list.get(tkinter.ANCHOR)
        indicator = indicator[0:5]
        indicator_content = capture_indicators.show_specific_indicator_of_specific_country(country, indicator)

        if len(indicator) == 0:
            self.text.delete(1.0, END)
            self.text.insert(END, f"Error\n\n{'X' * 10}\n\n Selecione uma opcao acima")
        else:
            self.list.delete(0, END)
            self.text.delete(1.0, END)

            self.list.insert(END, f"    **  {self.country_open.title()}({self.sigla_of_open_country})  **")
            self.list.insert(END, f" ")
            for i in indicator_content[0]:
                if i == "series":
                    for option in indicator_content[0][i][0]["serie"]:
                        self.text.insert(END, f"**{option}\n")
                else:
                    self.list.insert(END, f'-{i.upper()}:   {indicator_content[0][i]}')
                    self.list.insert(END, f" ")

            self.button_search.destroy()
            self.label_of_search.config(text=f"")

            self.button_return = Button(self.sub_frame_left)
            self.button_return.configure(font="Consolas 8 bold", text="voltar", bd=1,
                                         command=self.back_to_search_settings)
            self.button_return.grid(row=0, column=0)

    # //// ---  em desenvolvimento ----------  -------------------  -----------
    def abrir_continentes(self):
        continentes_existentes = capture_continents.mostrar_continentes_existentes()
        mostrar_paises = capture_continents.mostrar_paises_de_cada_continente()
        quantidade_de_paises = capture_continents.mostrar_numero_de_paises_de_cada_continente()

        self.list.config(state=NORMAL)
        for i in continentes_existentes:
            self.list.insert(END, f"{i}")

        self.text.insert(END, f"Quantidade de paises:\n")
        for i in quantidade_de_paises:
            self.text.insert(END, f"-{i}: {quantidade_de_paises[i]} paises\n")

        self.text.insert(END, f"\n\nPaises de cada continente:\n")
        for i in mostrar_paises:
            self.text.insert(END, f"* {i}:\n{mostrar_paises[i]}\n\n")

        self.button_search.config(text=f"Selecionar continente:")
        self.button_search.configure(command=self.selecionar_continente)
        self.label_of_search.config(text=f"Infomracoes sobre\ncontinente selecionado")
        self.entry_of_search.destroy()

    def selecionar_continente(self):
        pass
    # ---------------------------------  ---------------------------   -----------


start()
