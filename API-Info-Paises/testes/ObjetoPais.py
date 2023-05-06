
class ObjetoPais:

    def __init__(self, code_id, name):

        self.__code_id = code_id
        self.__name = name

        self.__area = dict()
        self.__location = dict()
        self.__languages = list()
        self.__government = dict()
        self.__currency_units = list()
        self.__historic = str()

    @property
    def code_id(self):
        return self.__code_id

    @property
    def name(self):
        return self.__name

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def languages(self):
        return self.__languages

    @languages.setter
    def languages(self, languages):
        self.__languages = languages

    @property
    def government(self):
        return  self.__government

    @government.setter
    def government(self, government):
        self.__government = government

    @property
    def currency_units(self):
        return self.__currency_units

    @currency_units.setter
    def currency_units(self, currency_units):
        self.__currency_units = currency_units

    @property
    def historic(self):
        return self.__historic

    @historic.setter
    def historic(self, historic):
        self.__historic = historic

