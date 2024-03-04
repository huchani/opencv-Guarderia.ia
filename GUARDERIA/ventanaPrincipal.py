
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import uic
from Admin import *
from Conexcion import Registro_datos
from Registro_Padre import RegistroPadre
from Registro_Usuario import RegistroUsuario
import cv2

class VentanaPrincipal():
    def __init__(self,admin,app) -> None:
        self.__Admin = admin
        self.__app = app
        self.registro = Registro_datos()
        self.login = uic.loadUi("InicioSesion.ui")
        self.menuU = uic.loadUi("menuUsuarios.ui")
        self.menuP = uic.loadUi("menuPadres.ui")

    def abrir(self):
        self.login.show()
        self.login.pushButton_3.clicked.connect(self.verificar)
        self.login.pushButton_4.clicked.connect(self.cerrar)
    
    def cerrar(self):
        self.login.hide()
        self.__app.exit()

    def verificar(self):
        usuario = self.login.lineEdit_4.text()
        clave = self.login.lineEdit_3.text()
        usuarios = self.registro.getUsuarios()

        if len(usuario)== 0 or len(clave)==0:
            print("los campos estan vacios.")
        elif (usuario == self.__Admin.getUsuario() and clave == self.__Admin.getClave()): 
            self.login.lineEdit_4.clear()      
            self.login.lineEdit_3.clear()   
            self.menuAdmin = RegistroUsuario(self.login)
            self.menuAdmin.menuAdmin()
            self.login.hide()            
            

        for user in range(len(usuarios)):
            if (usuario == usuarios[user][0] and clave == usuarios[user][1]):
                self.login.lineEdit_4.clear()      
                self.login.lineEdit_3.clear()
                self.menuProfe = RegistroPadre(self.login)
                self.menuProfe.menuPapa()
                self.login.hide()
                
        else:
            print("error..")
            print(self.__Admin.getUsuario())
            print(self.__Admin.getClave())
        #print(usuario)

     

    


app=QtWidgets.QApplication([])
admin = Administrador()
p = VentanaPrincipal(admin,app)
p.abrir()
app.exec()