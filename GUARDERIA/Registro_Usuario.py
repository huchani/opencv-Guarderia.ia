from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QPixmap
#from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from Admin import *
from Comun import Comun
from Conexcion import Registro_datos


class RegistroUsuario:
    def __init__(self, login):
        self.__lista_Usuarios=[]
        self.login = login
        self.registro = Registro_datos()
        self.menu = uic.loadUi("menuUsuarios.ui")

        self.menu.bt_regi.clicked.connect(self.obtenerDatosUsuario)
        self.menu.bt_refrescarRegistro.clicked.connect(self.MostrarUsuario)
        self.menu.bt_buscar_modi.clicked.connect(self.buscarUsuario)
        self.menu.bt_actualizar_modi.clicked.connect(self.actualizarDatosUsuario)
        self.menu.pushButton_3.clicked.connect(self.eliminar)

        self.menu.but_regresar.clicked.connect(self.volver)

    def menuAdmin(self):
        self.menu.show()
        self.menu.but_registrar.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.pag_Admin))

        self.menu.pushButton.clicked.connect(self.ocultarU)
        self.menu.bt_admin_registrar.clicked.connect(lambda: self.menu.stackedWidget_2.setCurrentWidget(self.menu.pagRegistrar))
        self.menu.bt_admin_bd.clicked.connect(lambda: self.menu.stackedWidget_2.setCurrentWidget(self.menu.pagBaseDatos))
        self.menu.bt_admin_modi.clicked.connect(lambda: self.menu.stackedWidget_2.setCurrentWidget(self.menu.pagModificar))

    def volver(self):
        self.menu.hide()
        self.login.show()
        
    def ocultarU(self):
        self.menu.frame_3.hide()
        self.menu.pushButton.clicked.connect(self.mostrarU)

    def mostrarU(self):
        self.menu.frame_3.show()
        self.menu.pushButton.clicked.connect(self.ocultarU)

    # REGISTRO DE USUARIOS
    def clear(self):
        self.menu.modi_nombre.clear()
        self.menu.modi_apellido.clear()
        self.menu.modi_CI.clear()
        self.menu.modi_edad.clear()
        self.menu.modi_telefono.clear()
        self.menu.modi_contrasenia.clear()

    def obtenerDatosUsuario(self):    
        user_Nombre = self.menu.regi_nombre.text()
        user_Apellido = self.menu.regi_apellido.text()
        user_ci = self.menu.regi_CI.text()
        user_edad = self.menu.regi_edad.text()
        user_telefono = self.menu.regi_telefono.text()
        user_usuario = self.menu.lineEdit_5.text()
        user_clave = self.menu.regi_contrasenia.text()
        if user_Nombre and user_Apellido and user_ci and user_edad and user_telefono and user_clave and user_usuario !="":
            comun = Comun(user_usuario,user_clave,user_Nombre,user_Apellido,int(user_ci),int(user_edad),int(user_telefono))
            existeCi = self.revisarCi(int(user_ci))
            if existeCi == True:
                self.menu.regi_signal.setText("¡La Persona Ya existe!")
            else:
                    self.__lista_Usuarios.append(comun)
                    self.menu.regi_nombre.clear()
                    self.menu.regi_apellido.clear()
                    self.menu.regi_CI.clear()
                    self.menu.regi_edad.clear()
                    self.menu.regi_telefono.clear()
                    self.menu.lineEdit_5.clear()
                    self.menu.regi_contrasenia.clear()
                    self.menu.regi_signal.setText("¡Registró con Exito!")
        else:
            self.menu.regi_signal.setText("¡Tódos los campos son obligatorios!")

    def revisarCi(self,ci):
        listaCi = self.registro.getCi()
        for buscar in listaCi:
            if ci == buscar[0]:
                return True
        else:
            return False
        
    def enviarDatosUsuario(self):
        for i in self.__lista_Usuarios:
            nombre = i.getNombre()
            apellido = i.getApellido()
            ci = i.getCi()
            edad = i.getEdad()
            telefono = i.getTelefono()
            user =i.getUsuario()
            clave = i.getClave()
            print(nombre,apellido,ci,edad,telefono,clave)
            self.registro.insert(nombre,apellido,ci,edad,telefono,user,clave)
        self.__lista_Usuarios.clear()

#LISTAR USUARIOS
    def MostrarUsuario(self):
        self.enviarDatosUsuario()
        datos_user = self.registro.mostrarTabla()
        fila= len(datos_user)
        self.menu.tablaBase.setRowCount(fila)
        tablaFila = 0
        #print("los datos")
        #print(datos_user)

        for dato in datos_user:
            self.menu.tablaBase.setItem(tablaFila,0,QtWidgets.QTableWidgetItem(dato[0]))
            self.menu.tablaBase.setItem(tablaFila,1,QtWidgets.QTableWidgetItem(dato[1]))
            self.menu.tablaBase.setItem(tablaFila,2,QtWidgets.QTableWidgetItem(str(dato[2])))
            self.menu.tablaBase.setItem(tablaFila,3,QtWidgets.QTableWidgetItem(str(dato[3])))
            self.menu.tablaBase.setItem(tablaFila,4,QtWidgets.QTableWidgetItem(str(dato[4])))
            self.menu.tablaBase.setItem(tablaFila,5,QtWidgets.QTableWidgetItem(dato[5]))
            self.menu.tablaBase.setItem(tablaFila,6,QtWidgets.QTableWidgetItem(dato[6]))
            
            tablaFila +=1


#ELIMINAR USUARIOS

    def eliminar(self):
        listaCi = self.registro.getCi()
        delCi = self.menu.lineEdit_3.text()
        print(len(listaCi))
        if delCi !='':
            print("hay algo")
            for Ci in range(len(listaCi)):
                if int(delCi) == listaCi[Ci][0]:
                    self.registro.eliminar(delCi)
                    self.menu.lineEdit.setText("Se elimino el Usuario!")
                    self.menu.lineEdit_3.clear()
                    break
            else:
                self.menu.lineEdit.setText("No existe el Usuario")
        else:
            self.menu.lineEdit.setText("Ingrese CI de Usuario!")
    
#EDITAR USUARIOS
    def buscarUsuario(self):
        aci = self.menu.line_modi.text()
        if aci == '':
            self.clear()
            self.menu.signal_modi.setText("introduzca CI")
        else:
            user = self.registro.buscar(int(aci))

            if user == []:
                self.clear()
                self.menu.signal_modi.setText("EL usuario no existe!")
            else:
                self.menu.signal_modi.clear()
                self.menu.modi_nombre.setText(user[0][1])
                self.menu.modi_apellido.setText(user[0][2])
                self.menu.modi_CI.setText(str(user[0][3]))
                self.menu.modi_edad.setText(str(user[0][4]))
                self.menu.modi_telefono.setText(str(user[0][5]))
                self.menu.lineEdit_4.setText(user[0][6])
                self.menu.modi_contrasenia.setText(user[0][7])

    def actualizarDatosUsuario(self):    
        aci = self.menu.line_modi.text()
        user_Nombre = self.menu.modi_nombre.text()
        user_Apellido = self.menu.modi_apellido.text()
        user_ci = self.menu.modi_CI.text()
        user_edad = self.menu.modi_edad.text()
        user_telefono = self.menu.modi_telefono.text()
        user_usuario = self.menu.lineEdit_4.text()
        user_clave = self.menu.modi_contrasenia.text()
        
        if user_Nombre and user_Apellido and user_ci and user_edad and user_telefono and user_usuario and user_clave !="":
                self.registro.actualizar(user_Nombre,user_Apellido,user_ci,user_edad,user_telefono,user_usuario,user_clave,aci)
                self.clear()
                self.menu.signal_modi.setText("¡Actualizó con Exito!")
        else:
            self.menu.signal_modi.setText("¡Tódos los campos son obligatorios!") 