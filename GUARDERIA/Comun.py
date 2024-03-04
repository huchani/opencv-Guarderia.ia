from Usuario import *
class Comun (Usuario):
    def __init__(self,usuario,clave,nombre="-",apellido="--",ci=0,edad=0,telefono=0):
        super().__init__(usuario,clave)
        self.__nombre = nombre 
        self.__apellido = apellido 
        self.__ci = ci
        self.__edad = edad
        self.__telefono = telefono

#getters
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCi(self):
        return self.__ci
    def getEdad(self):
        return self.__edad
    def getTelefono(self):
        return self.__telefono


#setters
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setApellido(self,apellido):
        self.__apellido = apellido
    def setCi(self,ci):
        self.__ci = ci
    def setEdad(self,edad):
        self.__edad = edad   
    def setTelefono(self,telefono):
        self.__telefono = telefono
  