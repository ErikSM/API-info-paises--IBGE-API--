class Country:

    def __init__(self, code_id, name, dict_of_attributes=None):
        self.__code_id = code_id
        self.__name = name

        self.__dict_of_attributes = dict_of_attributes

        if self.__dict_of_attributes is None:
            self.__location = {"continente": None,
                               "regiao": None,
                               "regiao especifica": None}
        elif self.__dict_of_attributes is not None:

            self.__location = self.__dict_of_attributes["localizacao"]
            self.__area = self.__dict_of_attributes["area"]
            self.__languages = self.__dict_of_attributes["linguas"]
            self.__government = self.__dict_of_attributes["governo"]
            self.__currency_units = self.__dict_of_attributes["unidade-monetaria"]

            self.__historic = self.__dict_of_attributes["historico"]

        self.error = False

        self.indicators = None

    def show_basic_informaton(self):
        if not self.error:
            return f'\n' \
                   f'id:  {self.__code_id}\n' \
                   f'nome: {self.__name}\n' \
                   f'localizacao:  {self.__location}' \
                   f'f\n'
        else:
            return f'Erro.[Country]'

    def show_all_informaton_about(self):
        if not self.error:
            return f'\n' \
                   f'id:  {self.__code_id}\n' \
                   f'nome: {self.__name}\n' \
                   f'localizacao:  {self.__location}\n' \
                   f'area:  {self.area}\n' \
                   f'linguas:  {self.__languages}\n' \
                   f'governo:  {self.__government}\n' \
                   f'unidade-monetaria:  {self.__currency_units}\n' \
                   f'historico: {self.__historic}\n' \
                   f'\n'
        else:
            return f'\n' \
                   f'id:  {self.__code_id}\n' \
                   f'nome: {self.__name}\n'

    @property
    def code_id(self):
        return self.__code_id

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    @property
    def area(self):
        return self.__area

    @property
    def languages(self):
        return self.__languages

    @property
    def government(self):
        return self.__government

    @property
    def currency_units(self):
        return self.__currency_units

    @property
    def historic(self):
        return self.__historic

    @property
    def dict_of_attributes(self):
        return self.__dict_of_attributes
