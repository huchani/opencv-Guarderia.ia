import cv2
import os
import numpy as np

class Entrenar:
    def guardar(self):
    
        dataPath ='C:/Users/Daniel/Documents/Guarderia_Final/GUARDERIA/fotos'
        peopleList = os.listdir(dataPath)
        print("lista de personas: ",peopleList)

        labels = []
        facesData = []
        label = 0

        for nameDir in peopleList :
            personPath = dataPath +'/'+nameDir
            print("leyendo las imagenes")

            for fileName in os.listdir(personPath):
                print("rostros: ",nameDir+'/'+fileName)
                labels.append(label)
                facesData.append(cv2.imread(personPath+'/'+fileName,0))
                image = cv2.imread(personPath+'/'+fileName,0)
            label +=1
            
        face_recognizer = cv2.face.EigenFaceRecognizer_create() #crea el reconnocedor
        #entenando el reconocedor de rostros 
        print("entrenando...")
        face_recognizer.train(facesData,np.array(labels))
        #almacenando el modelo obtenido
        face_recognizer.write('ModeloEntrenado.xml')
        print("Modelo Almacenado")