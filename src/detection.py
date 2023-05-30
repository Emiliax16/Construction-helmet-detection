import cv2

# Inicialización de la captura de video desde la cámara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Carga del clasificador de detección del objeto (en este caso, un archivo XML)
helmetClassif = cv2.CascadeClassifier('ruta/para/archivo/cascade.xml')

while True:
    # Captura del fotograma actual de la cámara
    ret, frame = cap.read()

    # Conversión a escala de grises para facilitar el procesamiento
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detección del casco utilizando el clasificador
    helmet = helmetClassif.detectMultiScale(gray,
                                           scaleFactor=5,
                                           minNeighbors=91,
                                           minSize=(70, 78))

    # Dibujo de un rectángulo y texto alrededor de todos los objetos detectados
    for (x, y, w, h) in helmet:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Casco', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    # Mostrar el fotograma actual en una ventana llamada 'frame'
    cv2.imshow('frame', frame)

    # Romper el bucle si se presiona la tecla Esc (27)
    if cv2.waitKey(1) == 27:
        break

# Liberar los recursos de la captura de video y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
