from persona import Persona
from deportista import Deportista



class Futbolista(Persona,Deportista):
    listaFutbolistas = []
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil

        Futbolista.listaFutbolistas.append(self)

    def setGolesMarcados(self, xd):
        self._golesMarcados = xd

    def getGolesMarcados(self):
        return self._golesMarcados


    def setTarjetasRojas(self, xd):
        self._tarjetasRojas = xd

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setPiernaHabil(self, xd):
        self._piernaHabil = xd

    def getPiernaHabil(self):
        return self._piernaHabil

    def __str__(self):
        return "Mi nombre es " +str(self.getNombre())+" soy profesional en el deporte "+str(self.getDeporte())+" Tengo "+str(self.getEdad())+" años de edad y llevo " + str(self.getAñosPracticando())+" años en el deporte"



