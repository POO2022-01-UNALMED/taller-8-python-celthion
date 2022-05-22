class Persona:
    def __init__(self,nombre,edad,altura,sexo):
        self._nombre=nombre
        self._edad=edad
        self._altura=altura
        self._sexo=sexo


    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setEdad(self, xd):
        self._edad = xd

    def getEdad(self):
        return self._edad

    def setAltura(self, xd):
        self._altura = xd

    def getAltura(self):
        return self._altura

    def setSexo(self, xd):
        self._sexo = xd

    def getSexo(self):
        return self._sexo

alfa = Persona("d","d",3,4)
alfa.getNombre()


