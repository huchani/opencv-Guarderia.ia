from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import os
import sys

class Reconocer :

    def __init__(self,ventana):
        self.ventana= ventana
        
    def conocer(self):

        dataPath = 'D:/proyetos_opencv/Guarderia_Final/GUARDERIA/fotos'
        imagePaths = os.listdir(dataPath)
        print('imagePaths= ',imagePaths)

        face_recognizer = cv2.face.EigenFaceRecognizer_create()
        face_recognizer.read('ModeloEntrenado.xml')

        cap = cv2.VideoCapture(0)

        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

        while True:
            ret,frame = cap.read()
            if ret == False :
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()
            faces = faceClassif.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces :
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                result = face_recognizer.predict(rostro)

                cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        		#EigenFaces
                if result[1] <5700:
                    cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

                else:
                    cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertir_QT =QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pic = convertir_QT.scaled(500,800, Qt.KeepAspectRatio)
            self.ventana.label_13.setPixmap(QPixmap.fromImage(pic))

        
            if cv2.waitKey(1) & 0xFF == ord('x'):
                print('aqui estoy................')
                break
        cap.release()
        cv2.destroyAllWindows()