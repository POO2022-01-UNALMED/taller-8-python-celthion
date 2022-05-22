class Deportista:

    def __init__(self,añosPracticando):

        self._deporte="Futbol"
        self._añosPracticando=añosPracticando

    def setDeporte(self, xd):
        self._deporte = xd

    def getDeporte(self):
        return self._deporte

    def setAñosPracticando(self, xd):
        self._añosPracticando = xd

    def getAñosPracticando(self):
        return self._añosPracticando
