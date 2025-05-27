from datetime import datetime, timedelta

class Treino:
    def __init__(self, data:datetime, dist:int, tempo:timedelta):
        self.data = data
        self.dist = dist
        self.tempo = tempo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, datetime):
            raise TypeError("data must be a datetime")
        self.__data = data


smart = Treino(14,3,4)