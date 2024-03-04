from Usuario import *

class Administrador (Usuario):
    def __init__(self,usuario="huchani",clave="4321"):
        super().__init__(usuario,clave)

    
#h = Administrador()
#print(h.getUsuario())
#print(h.getClave())