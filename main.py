import cv2
import time

import pygame

#thres = 0.45 # Threshold to detect object

# Variables globales
human_detected = False  # Indica si se ha detectado un humano recientemente
human_timer = 0  # Temporizador para controlar el tiempo de espera después de detectar un humano
human_printed = False  # Indica si se ha impreso el mensaje "HUMANO SIN TAZA!" recientemente
cup_detected = False  # Indica si se ha detectado una taza recientemente


classNames = []
classFile = "db/object_detect/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "db/object_detect/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "db/object_detect/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return img,objectInfo


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    #cap.set(10,70)
    pygame.mixer.init()
    # Ruta del archivo WAV
    ruta_archivo_wav = "DEFINITIVO.wav"
    pygame.mixer.music.load(ruta_archivo_wav)

    while True:
        success, img = cap.read()
        result, objectInfo = getObjects(img,0.45,0.2, objects=['cup', 'person'])

        if success:
            if len(objectInfo) > 0 and not human_detected:
                # Buscamos si hay un humano
                for obj in objectInfo:
                    for name in obj:
                        if isinstance(name, str) and name == 'person':
                            print("HUMANO DETECTADO!")
                            human_detected = True
                            human_timer = time.time()
                            human_printed = False
                            break
                    if human_detected:
                        break
            elif len(objectInfo) > 0 and human_detected:
                # Chequeamos si ya pasaron 3 segundos
                if time.time() - human_timer <= 4 and not cup_detected:
                    # Chequeamos si hay una taza
                    for obj in objectInfo:
                        for name in obj:
                            if isinstance(name, str) and name == 'cup':
                                cup_detected = True
                                print("HUMANO CON SEUDO CASCO!")
                                break
                        if cup_detected:
                            break
                elif time.time() - human_timer > 4 and time.time() - human_timer <= 12 and not human_printed and not cup_detected:
                    if not cup_detected:
                        if not human_printed:
                            print("HUMANO SIN SEUDO CASCO!")
                            human_printed = True
                            pygame.mixer.music.play()
                elif time.time() - human_timer > 12:
                    human_detected = False
                    cup_detected = False
                    human_printed = False
                    human_timer = 0
                    
            cv2.imshow("Output",img)
        cv2.waitKey(1)
