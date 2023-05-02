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

        # // paises
        self.menu_countries = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Paises", menu=self.menu_countries)
        self.menu_countries.add_command(label="Lista de Paises", command=self.open_countries)

        # // continentes(em desenvolvimento)
        self.menu_continents = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Continentes", menu=self.menu_continents)
        self.menu_continents.add_command(label="Lista de Continentes", command=self.open_continents)

        self.frame = Frame(self.window, bg="grey90")
        self.frame.pack()
        self.text = Text(self.window, font="Arial 9 bold", width=100, height=20, bg="grey90", bd=3)
        self.text.pack()

        self.sub_frame_left = Frame(self.frame, bg="grey90")
        self.sub_frame_left.pack(side="left")
        self.sub_frame_right = Frame(self.frame, bg="grey90")
        self.sub_frame_right.pack(side="right")

        self.label_of_list = Label()
        self.label_of_button = Label()
        self.button_action = Button()
        self._initial_settings()

        self.list = Listbox(self.sub_frame_right, width=90, height=9, bd=2, bg="grey90")
        self.list.grid(row=1, column=0)
        self.list.config(state=tkinter.DISABLED)

        self.window.mainloop()

    def _initial_settings(self):
        self.label_of_list.destroy()
        self.label_of_list = Label(self.sub_frame_right)
        self.label_of_list.configure(text="-----------   ----------- :", bg="grey90")
        self.label_of_list.grid(row=0, column=0)

        self.label_of_button.destroy()
        self.label_of_button = Label(self.sub_frame_left, font="Arial 7 bold", bg="grey90")
        self.label_of_button.configure(text="Abra a lista no menu acima:")
        self.label_of_button.grid(row=0, column=0, columnspan=2)

        self.button_action.destroy()
        self.button_action = Button(self.sub_frame_left)
        self.button_action.configure(font="Consolas 8 bold", text="Busca", bd=1, command=self.search)
        self.button_action.grid(row=1, column=1)
        self.button_action.config(state=DISABLED)

    def _back_to_initial_settings(self):
        start(self.window)

    def search(self):
        self.label_of_list.destroy()
        self.label_of_list = Label(self.sub_frame_right)
        self.label_of_list.configure(text=f"Infomacoes Basicas:", bg="grey90")
        self.label_of_list.grid(row=0, column=0)

        self.label_of_button.destroy()
        self.label_of_button = Label(self.sub_frame_left, font="Arial 7 bold", bg="grey90")
        self.label_of_button.configure(text="Clique para saber mais:")
        self.label_of_button.grid(row=0, column=0, columnspan=2)

        self.button_action.destroy()
        self.button_action = Button(self.sub_frame_left, font="Consolas 8 bold", bd=1)
        self.button_action.configure(text=f"<Informacoes avancadas>", command=self._advanced_information_about_country)
        self.button_action.grid(row=1, column=1)

        self.list.config(state=tkinter.NORMAL)

        select_from_list = self.list.get(tkinter.ANCHOR)
        self.country_select = select_from_list[0:2]

        if len(self.country_select) == 0:
            self.text.delete(1.0, END)
            self.list.delete(0, END)

            self.list.insert(END, f"   {'X' * 10} ")
            self.list.insert(END, "   %##$  Informacoes nao encontradas ou Imprecisas   #$%& ")
            self.text.insert(1.0, f"\n\n{'X' * 10}\n\n      #$%& ErRor #$%& ")
        else:
            try:
                request = requests.get(f""
                                       f"https://servicodados.ibge.gov.br/api/v1/paises/"
                                       f"{self.country_select}"
                                       )

                dict_of_search = json.loads(request.text)

                self.text.delete(1.0, END)
                self.list.delete(0, END)

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

                    self.country_open = item["nome"]["abreviado"]
                    self.country_open = self.country_open.lower()
            except Exception as ex:
                self.text.delete(1.0, END)
                self.list.delete(0, END)

                self.text.config(bg="grey70")
                self.list.config(bg="grey70")

                self.list.insert(END, "XXX error xx")
                self.list.insert(END, f"--{ex}---")

                self.label_of_button.configure(text="Error! volte ao inicio")
                self.button_action.configure(text=f"voltar",
                                             command=self._back_to_initial_settings)

            self.sigla_of_open_country = self.country_select

    def _advanced_information_about_country(self):
        self.label_of_list.destroy()
        self.label_of_list = Label(self.sub_frame_right)
        self.label_of_list.configure(text=f"{self.country_open.title()}", bg="grey90")
        self.label_of_list.grid(row=0, column=0)

        self.label_of_button.destroy()
        self.label_of_button = Label(self.sub_frame_left, font="Arial 7 bold", bg="grey90")
        self.label_of_button.configure(text="Selecione um indicador ao lado:")
        self.label_of_button.grid(row=0, column=0, columnspan=2)

        self.button_action.destroy()
        self.button_action = Button(self.sub_frame_left, font="Consolas 8 bold", bd=1)
        self.button_action.configure(text=f"Especificar indicador", command=self._show_selected_indicator)
        self.button_action.grid(row=1, column=1)

        all_indicators = capture_indicators.show_indicators_id()
        country_indicators = capture_indicators.show_all_indicators_of_selected_country(self.sigla_of_open_country)

        self.list.config(state=tkinter.NORMAL)

        self.list.delete(0, END)
        self.text.delete(1.0, END)

        for i in all_indicators:
            indicator = i
            indicator_code = all_indicators[i]
            self.list.insert(END, f"{indicator_code}:  {indicator}")

        for i in country_indicators:
            try:
                indicator = f"({i['id']}){i['indicador']}: {i['series'][0]['pais']}"
                information = f"{i['series'][0]['serie']}"
            except Exception as ex:
                indicator = f"({i['id']}){i['indicador']}: {i['series']}- error{ex}??"
                information = f"{i['series']}error{ex} -- Conteudo inexistente"
            self.text.insert(END, f"{indicator}\n")
            self.text.insert(END, f"{information}\n\n")

    def _show_selected_indicator(self):
        self.label_of_list.destroy()
        self.label_of_list = Label(self.sub_frame_right)
        self.label_of_list.configure(text="fonte: IBGE", bg="grey90")
        self.label_of_list.grid(row=0, column=0)

        self.label_of_button.destroy()
        self.label_of_button = Label(self.sub_frame_left, font="Arial 7 bold", bg="grey90")
        self.label_of_button.configure(text="Clique para voltar ao inicio:")
        self.label_of_button.grid(row=0, column=0, columnspan=2)

        self.button_action.destroy()
        self.button_action = Button(self.sub_frame_left, font="Consolas 8 bold", bd=1)
        self.button_action.configure(text="voltar", command=self._back_to_initial_settings)
        self.button_action.grid(row=1, column=1)

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
                    try:
                        for option in indicator_content[0][i][0]["serie"]:
                            self.text.insert(END, f"**{option}\n")
                    except Exception as ex:
                        self.text.insert(END, f"ERRor {ex} \n\n Conteudo inexistente")
                else:
                    self.list.insert(END, f'-{i.upper()}:   {indicator_content[0][i]}')
                    self.list.insert(END, f" ")

    def open_countries(self):
        self.label_of_list.destroy()
        self.label_of_list = Label(self.sub_frame_right)
        self.label_of_list.configure(text="Paises:", bg="grey90")
        self.label_of_list.grid(row=0, column=0)

        self.label_of_button.destroy()
        self.label_of_button = Label(self.sub_frame_left, font="Arial 7 bold", bg="grey90")
        self.label_of_button.configure(text="Selecione um pais ao lado:")
        self.label_of_button.grid(row=0, column=0, columnspan=2)

        self.button_action.destroy()
        self.button_action = Button(self.sub_frame_left)
        self.button_action.configure(font="Consolas 8 bold", text="Busca", bd=1, command=self.search)
        self.button_action.grid(row=1, column=1)

        self.list.config(state=tkinter.NORMAL)

        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
        dict_of_indexes = json.loads(request.text)

        self.list.delete(0, END)
        self.text.delete(1.0, END)

        self.text.config(bg="grey90")
        self.list.config(bg="grey70")

        for country in dict_of_indexes:
            self.list.insert(END, f"{country['id']['ISO-ALPHA-2']}:"
                                  f" {country['nome']}{' ' * 2}\n")
            for i in country:
                if i == "id":
                    pass
                else:
                    self.text.insert(END, f"{i}: {country[i]}    ")
            self.text.insert(END, f"\n{'-'*20}\n")

    def open_continents(self):
        self.label_of_list.destroy()
        self.label_of_list = Label(self.sub_frame_right)
        self.label_of_list.configure(text="Continentes:", bg="grey90")
        self.label_of_list.grid(row=0, column=0)

        self.label_of_button.destroy()
        self.label_of_button = Label(self.sub_frame_left, font="Arial 7 bold", bg="grey90")
        self.label_of_button.configure(text=f"Selecione um continente ao lado:")
        self.label_of_button.grid(row=0, column=0, columnspan=2)

        self.button_action.destroy()
        self.button_action = Button(self.sub_frame_left, font="Consolas 8 bold", bd=1)
        self.button_action.configure(text=f"Selecionar continente:", command=lambda: self._select_continent(
            all_countries_of_one_continent, number_of_contries_from_each))
        self.button_action.grid(row=1, column=1)

        all_continents = capture_continents.show_all_continents()
        all_countries_of_one_continent = capture_continents.show_contries_each_continent()
        number_of_contries_from_each = capture_continents.show_number_of_countries_from_each_continent()

        self.list.config(state=NORMAL)
        self.list.delete(0, END)
        self.text.delete(1.0, END)

        for continent in all_continents:
            self.list.insert(END, f"{continent}")

        self.text.insert(END, f"Quantidade de paises:\n")
        for continent in number_of_contries_from_each:
            self.text.insert(END, f"-{continent}: {number_of_contries_from_each[continent]} paises\n")

        self.text.insert(END, f"\n\nPaises de cada continente:\n")
        for continent in all_countries_of_one_continent:
            self.text.insert(END, f"* {continent}:\n{all_countries_of_one_continent[continent]}\n\n")

    def _select_continent(self, mostrar_paises, quantidade_de_de_paises):
        self.label_of_button.destroy()
        self.label_of_button = Label(self.sub_frame_left, font="Arial 7 bold", bg="grey90")
        self.label_of_button.configure(text=f"Clique para infomracoes sobre\n o pais selecionado")
        self.label_of_button.grid(row=0, column=0, columnspan=2)

        self.button_action.destroy()
        self.button_action = Button(self.sub_frame_left, font="Consolas 8 bold", bd=1)
        self.button_action.configure(text=f"Busca:", command=self.search)
        self.button_action.grid(row=1, column=1)

        continente_selecionado = self.list.get(tkinter.ANCHOR)

        self.text.delete(1.0, END)
        self.text.insert(END, f"- {continente_selecionado}:\n")
        self.text.insert(END, f"Este continente possui um total de "
                              f"{quantidade_de_de_paises[continente_selecionado]} paises.")

        self.list.delete(0, END)
        for pais in mostrar_paises[continente_selecionado]:
            self.list.insert(END, f"{pais}\n")

start()
