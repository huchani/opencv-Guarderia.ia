
class Padre:
    def __init__(self,nombre_ninio, nombre_padre, apellido, ci, edad, telefono, direccion) -> None:
        self.__nombre_ninio = nombre_ninio
        self.__nombre_padre = nombre_padre
        self.__apellido = apellido
        self.__ci = ci
        self.__edad = edad
        self.__telefono = telefono
        self.__direccion = direccion

    #getters
    def getNombre_ninio(self):
        return self.__nombre_ninio
    
    def getNombre_padre(self):
        return self.__nombre_padre

    def getApellido(self):
        return self.__apellido

    def getCi(self):
        return self.__ci

    def getEdad(self):
        return self.__edad

    def getTelefono(self):
        return self.__telefono

    def getDireccion(self):
        return self.__direccion

    #setters
    def setNombre_ninio(self, nombre_ninio):
        self.__nombre_ninio = nombre_ninio
    
    def setNombre_padre(self, nombre_padre):
        self.__nombre_padre = nombre_padre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def setCi(self, ci):
        self.__ci = ci

    def setEdad(self, edad):
        self.__edad = edad

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def setDireccion(self, direccion):
        self.__direccion = direccion