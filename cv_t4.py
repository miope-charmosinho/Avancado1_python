import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    ret, fr = cap.read()

    img = cv2.line(frame, (0,0),(frame.shape[1],frame.shape[0]), (0,0,0), 10)       # file / posição inicial / posição final / cor / espessura
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,0), 4)        # file / canto superior esquerdo / canto inferior direito / cor / espessura
    img = cv2.circle(img, ((img.shape[1])//2,(img.shape[0])//2), 32, (0,0,255), -1)     # Passar "-1" como argumento de espessura preenche a forma
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Texto incrivel', (130, 470), font, 1.5, (0,255,128), 5, cv2.LINE_AA)      # file / 'texto' / posição de inicio / fonte / tamanho da fonte / cor / espessura / não sei

    cv2.imshow('frame', fr)
    if cv2.waitKey(1) == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()