
class Indicator:

    def __init__(self, code, name, unit):

        self.__code = code
        self.__name = name
        self.__unit = unit

        self.__series = list()

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def unit(self):
        return self.__unit

    @property
    def series(self):
        return  self.__series

    @series.setter
    def series(self, series):
        self.__series = series
