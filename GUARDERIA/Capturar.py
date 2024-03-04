
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import os
import imutils

class Capturar():
    def __init__(self,nombre,ventana):
        self.nombre = nombre
        self.ventana =ventana
        
    def guardar(self):    
        personName = self.nombre 
        dataPath = 'C:/Users/Daniel/Documents/Guarderia_Final/GUARDERIA/fotos'
        personPath = dataPath+'/'+personName  
        print('--> ',personPath)
        
        if not os.path.exists(personPath):
            print('Carpeta Creada: ',personPath)  
            os.makedirs(personPath)
        
        cap = cv2.VideoCapture(0)
        
        faceClassif =  cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') 
        count = 0
        
        while True:
            ret, frame = cap.read()
            if ret == False:
                break

            else:
                frame = imutils.resize(frame,width=900)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = frame.copy()
                faces = faceClassif.detectMultiScale(gray,1.3,5)
                
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150),interpolation = cv2.INTER_CUBIC)
                    cv2.imwrite(personPath+'/rostro_{}.jpg'.format(count),rostro)
                    count +=1 

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertir_QT =QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pic = convertir_QT.scaled(500,800, Qt.KeepAspectRatio)
                self.ventana.label_7.setPixmap(QPixmap.fromImage(pic))
                
                k =cv2.waitKey(1)
                if k == 27 or count >=300:
                    self.ventana.label_7.clear()
                    break