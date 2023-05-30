import cv2
import numpy as np
import imutils
import os

Datos = 'ruta a la carpeta donde queremos guardar todas las imágenes capturadas (se le aplica ya resize)'
no_resize = 'ruta donde se deja la imagen tal cual se recolecta'

# Si no encuentra las rutas anteriores, crea las carpetas
if not os.path.exists(Datos):
    print('Carpeta creada: ',Datos)
    os.makedirs(Datos)

if not os.path.exists(no_resize):
    print('Carpeta creada: ', no_resize)
    os.makedirs(no_resize)

# se inicia la cámara del computador, es posible pasarle otras cámaras
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


# Se definen las coordenadas del cuadro verde que capturará la imagen
x1, y1 = 280, 190
x2, y2 = 360, 240

# Se itera infinitamente dentro del while para estar capturando cada imagen en tiempo real
count = 0
while True:

    # Se lee la imagen, si ret es false significa que hay un error en la lectura.
    # Frame guarda la imagen
    ret, frame = cap.read()
    if ret == False: break
    imAux = frame.copy()
    # Dibujo un rectángulo verde
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

    objeto = imAux[y1:y2,x1:x2]
    objeto_ = imAux[y1:y2,x1:x2]

    # Se le hace un resize al objeto capturado
    objeto = imutils.resize(objeto,width=200)

    # Al presionar la tecla s, se guarda la imagen
    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
        cv2.imwrite(no_resize+'/objeto_{}.jpg'.format(count),objeto_)
        print('Imagen guardada:'+'/objeto_{}.jpg'.format(count))
        count = count +1
    # Al presionar la tecla ESC, se cierra el programa
    if k == 27:
        break
    
    # imshow va mostrando el video y el objeto (rectángulo verde)
    cv2.imshow('frame',frame)
    cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()