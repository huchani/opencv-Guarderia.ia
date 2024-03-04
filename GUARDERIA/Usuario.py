
class Usuario:
    def __init__(self,usuario,clave):
        self.__usuario = usuario 
        self.__clave = clave

    def getUsuario (self):
        return self.__usuario
    
    def getClave (self):
        return self.__clave
    
    def setUsuario (self,nuevo):
        self.__usuario = nuevo
    
    def setClave (self,nuevo):
        self.__clave = nuevo

