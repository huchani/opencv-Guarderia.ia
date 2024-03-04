from Conexcion import Registro_datos
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import uic
from Padre import Padre
from Capturar import *
from EntrenarXML import *
from Reconocer import *
import cv2

class RegistroPadre():
    def __init__(self,login) -> None:
        self.__listaPadres = []
        self.login = login
        self.base_datos=Registro_datos()
        self.menu = uic.loadUi("menuPadres.ui")
        self.menu.bt_regi_2.clicked.connect(self.registroPadre)
        self.menu.bt_refrescarRegistro_2.clicked.connect(self.mostrarPadres)
        self.menu.bt_buscar_modi_2.clicked.connect(self.buscar)
        self.menu.bt_actualizar_modi_2.clicked.connect(self.actualizar)
        self.menu.bt_buscar_modi_3.clicked.connect(self.eliminar)
        self.menu.pushButton_3.clicked.connect(self.capturar)
        self.menu.bt_regi_3.clicked.connect(self.entrenar)
        self.menu.pushButton.clicked.connect(self.reconocer)
        #self.menu.pushButton_4.clicked.connect(self.stop)
        self.menu.but_regresar.clicked.connect(self.volver)

    def menuPapa(self):
        self.menu.show()
        self.menu.but_base_datos.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.pag_RegiPadre))
        self.menu.but_modificar.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.pag_Facial))

        self.menu.pushButton_5.clicked.connect(self.ocultarP)
        self.menu.pushButton_6.clicked.connect(lambda: self.menu.stackedWidget_3.setCurrentWidget(self.menu.pagRegistrar_2))
        self.menu.pushButton_7.clicked.connect(lambda: self.menu.stackedWidget_3.setCurrentWidget(self.menu.pagBaseDatos_2))
        self.menu.pushButton_8.clicked.connect(lambda: self.menu.stackedWidget_3.setCurrentWidget(self.menu.pagModificar_2))
        self.menu.but_modificar.clicked.connect(lambda: self.menu.stackedWidget_3.setCurrentWidget(self.menu.pag_Facial))

    def volver(self):
        self.menu.hide()
        self.login.show()

    def ocultarP(self):
        self.menu.frame_8.hide()
        self.menu.pushButton_5.clicked.connect(self.mostrarP)

    def mostrarP(self):
        self.menu.frame_8.show()
        self.menu.pushButton_5.clicked.connect(self.ocultarP)

#VISION
    def capturar(self):
        nombre = self.menu.regi_ninio_2.text()
        captura = Capturar(nombre,self.menu)
        captura.guardar()

    def entrenar(self):
        train =Entrenar()
        train.guardar()

    def reconocer(self):
        conocer = Reconocer(self.menu)
        conocer.conocer()




#CRUD PADRE
    def registroPadre(self):
        nombre_ninio = self.menu.regi_ninio_2.text()
        nombre_padre = self.menu.regi_padre_2.text()
        apellido = self.menu.regi_apellido_2.text()
        ci = self.menu.regi_CI_2.text()
        edad = self.menu.regi_edad_2.text()
        telefono = self.menu.regi_telefono_2.text()
        direccion = self.menu.regi_direccion_2.text()
        if nombre_ninio!='' and nombre_padre!='' and apellido!='' and ci!='' and edad!='' and telefono!='' and direccion!='':  #comprobar campos vacios
            padre = Padre(nombre_ninio,nombre_padre,apellido,int(ci),int(edad),int(telefono),direccion)
            self.__listaPadres.append(padre)
            self.menu.regi_signal_2.setText("Registro Exitoso")
            self.menu.regi_ninio_2.clear()
            self.menu.regi_padre_2.clear()
            self.menu.regi_apellido_2.clear()
            self.menu.regi_CI_2.clear()
            self.menu.regi_edad_2.clear()
            self.menu.regi_telefono_2.clear()
            self.menu.regi_direccion_2.clear()
        else:
            self.menu.regi_signal_2.setText("Faltan Datos")

    def enviarDatos(self):
        for i in self.__listaPadres:
            nombre_ninio = i.getNombre_ninio()
            nombre_padre = i.getNombre_padre()
            apellido = i.getApellido()
            ci = i.getCi()
            edad = i.getEdad()
            telefono = i.getTelefono()
            direccion = i.getDireccion()
            self.base_datos.instertarPadre(nombre_ninio,nombre_padre,apellido,ci,edad,telefono,direccion)
        self.__listaPadres.clear()

    def mostrarPadres(self):
        self.enviarDatos()
        datos = self.base_datos.mostrarPadre()
        i = len(datos)
        self.menu.tablaBase_2.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.menu.tablaBase_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.menu.tablaBase_2.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.menu.tablaBase_2.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.menu.tablaBase_2.setItem(tablerow,3,QtWidgets.QTableWidgetItem(str(row[3])))
            self.menu.tablaBase_2.setItem(tablerow,4,QtWidgets.QTableWidgetItem(str(row[4])))
            self.menu.tablaBase_2.setItem(tablerow,5,QtWidgets.QTableWidgetItem(str(row[5])))
            self.menu.tablaBase_2.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
            tablerow += 1

    def buscar(self):
        buscar= self.menu.line_modi_2.text()
        if buscar=='':
            self.menu.signal_modi_2.setText("no ingreso CI")
        else:
            dato=self.base_datos.buscarPadre(buscar)
            if dato==[]:
                self.menu.signal_modi_2.setText("no existe la persona")
            else: 
                self.menu.signal_modi_2.clear()
                self.menu.modi_ninio_2.setText(dato[0][1])
                self.menu.modi_padre_2.setText(dato[0][2])
                self.menu.modi_apellid_2.setText(dato[0][3])
                self.menu.modi_CI_2.setText(str(dato[0][4]))
                self.menu.modi_edad_2.setText(str(dato[0][5]))
                self.menu.modi_telefono_2.setText(str(dato[0][6]))
                self.menu.modi_direccion_2.setText(dato[0][7])

    def actualizar(self):
        
        buscar=self.menu.line_modi_2.text()
        nombreN=self.menu.modi_ninio_2.text()
        nombreP=self.menu.modi_padre_2.text()
        apellido=self.menu.modi_apellid_2.text()
        ci=self.menu.modi_CI_2.text()
        edad=self.menu.modi_edad_2.text()
        telefono=self.menu.modi_telefono_2.text()
        direccion=self.menu.modi_direccion_2.text()

        if nombreN!='' and nombreP!='' and apellido!='' and ci!='' and edad!='' and telefono!='' and direccion!='': 
            self.menu.modi_padre_2.clear()
            self.menu.modi_apellid_2.clear()
            self.menu.modi_CI_2.clear()
            self.menu.modi_edad_2.clear()
            self.menu.modi_telefono_2.clear()
            self.menu.modi_direccion_2.clear()
            self.menu.modi_ninio_2.clear()
            self.menu.line_modi_2.clear()
            self.base_datos.actualizarPadre(nombreN,nombreP,apellido,int(ci),int(edad),int(telefono),direccion,int(buscar))
            self.menu.signal_modi_2.setText ("cambio exitoso ")
            self.menu.lineEdit_2.clear()
        
        else:
            self.menu.signal_modi_2.setText ("Faltam Datos ")
    
    def eliminar(self):
        listaCi = self.base_datos.getCiPapa()
        delCi = self.menu.line_modi_3.text()
        print(len(listaCi))
        if delCi !='':
            print("hay algo")
            for Ci in range(len(listaCi)):
                if int(delCi) == listaCi[Ci][0]:
                    self.base_datos.eliminarPapa(delCi)
                    self.menu.lineEdit_2.setText("Se elimino el Usuario!")
                    self.menu.line_modi_3.clear()
                    break
            else:
                self.menu.lineEdit_2.setText("No existe el Usuario")
        else:
            self.menu.lineEdit_2.setText("Ingrese CI de Usuario!")


        


#app=QtWidgets.QApplication([])
#p = VentanaPrincipal()
#p.menu1()
#app.exec_()

