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
        print("Mi nombre es",Persona.getNombre(self) , "soy profesional en el deporte", Deportista.getDeporte(self) ,"Tengo" ,Persona.getEdad(self), "años de edad y llevo" ,Deportista.getAñosPracticando(self) ,"Participando años en el deporte")



futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
futbolista.__str__()