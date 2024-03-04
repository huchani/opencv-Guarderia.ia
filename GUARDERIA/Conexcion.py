
import mysql.connector

class Registro_datos():
    def __init__(self) -> None:
        self.conexion = mysql.connector.connect(host = 'localhost', database = 'guarderia', user = 'root', password = '2468')

    def instertarPadre(self, nombre_ninio, nombre_padre, apellido, ci, edad, telefono, direccion):
        cursor =self.conexion.cursor()
        cursor.execute("INSERT INTO padres (Nombre_niño,Nombre_padre,Apellido,Ci,Edad,Telefono,Direccion) VALUES('{}','{}','{}',{},{},{},'{}')".format(nombre_ninio,nombre_padre,apellido,ci,edad,telefono,direccion))
        self.conexion.commit()
        cursor.close()

    def mostrarPadre(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT Nombre_niño,Nombre_padre,Apellido,Ci,Edad,Telefono,Direccion FROM padres")
        registro = cursor.fetchall()
        cursor.close()
        return registro

    def buscarPadre(self,ci):
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM padres WHERE Ci= {} ".format(ci))
        registro=cursor.fetchall()
        cursor.close()
        return registro

    def actualizarPadre(self,nombre_ninio,nombre_padre,apellido,ci,edad,telefono,direccion,ci2):
        cursor=self.conexion.cursor()
        cursor.execute("UPDATE padres SET Nombre_niño= '{}' , Nombre_padre= '{}' , Apellido= '{}' , Ci= {}, Edad = {} , Telefono= {} , Direccion = '{}' WHERE Ci= {} ".format(nombre_ninio,nombre_padre,apellido,ci,edad,telefono,direccion,ci2))
        self.conexion.commit()
        cursor.close()
    
    def eliminarPapa(self,ci): #se elimina con ci
        cursor  = self.conexion.cursor()
        cursor.execute("DELETE from padres where ci ={}".format(ci))
        self.conexion.commit()
        cursor.close()
    
    def getCiPapa(self):
        cursor =self.conexion.cursor()
        cursor.execute("SELECT ci FROM padres")
        ci = cursor.fetchall()
        cursor.close()
        return ci

    def insert(self,nombre,apellido,ci,edad,telefono,user,clave):
        cursor = self.conexion.cursor() #declaramos una var de tipo cursor 
        cursor.execute("INSERT INTO usuario (nombre,apellido,ci,edad,telefono,usuario,clave) VALUES('{}','{}',{},{},{},'{}','{}')".format(nombre,apellido,ci,edad,telefono,user,clave))
        self.conexion.commit() # para enviar datos 
        cursor.close() #cerramos el cursor
    
    def mostrarTabla(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, apellido, ci, edad, telefono, usuario, clave FROM usuario")
        registro = cursor.fetchall() #para recibir datos
        cursor.close()
        return registro
    
    def buscar(self,aci):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuario WHERE ci={}".format(aci))
        registro = cursor.fetchall()
        cursor.close()
        return registro

    def getUsuarios(self): #obtiene el nombre
        cursor = self.conexion.cursor()
        cursor.execute("SELECT usuario, clave FROM usuario")
        user = cursor.fetchall()
        cursor.close()
        return user

    def eliminar(self,ci): #se elimina con ci
        cursor  = self.conexion.cursor()
        cursor.execute("DELETE from usuario where ci ={}".format(ci))
        self.conexion.commit()
        cursor.close()
    
    def actualizar(self,nombre,apellido,ci,edad,telefono,user,clave,aci):
        cursor =self.conexion.cursor()
        cursor.execute("UPDATE usuario set nombre ='{}',apellido ='{}', ci ={}, edad ={}, telefono={},usuario='{}',clave='{}' where ci = {}".format(nombre,apellido,ci,edad,telefono,user,clave,aci))
        self.conexion.commit()
        cursor.close()
    
    def getCi(self):
        cursor =self.conexion.cursor()
        cursor.execute("SELECT ci FROM usuario")
        ci = cursor.fetchall()
        cursor.close()
        return ci
    
reg = Registro_datos()
print(reg.getCi())