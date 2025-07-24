import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()         # se 'frame' nã retornar uma imagem 'ret' é "False" e mata o loop (*estudar tuplas)

    menor_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)

    img = np.zeros(frame.shape, np.uint8)       # np.uint8 = usigned integer 8 bits = Tipo especifico que esse array numpy quer receber
    tam = menor_frame.shape

    for i in range(0,img.shape[0],tam[0]):
        for j in range(0,img.shape[1],tam[1]):
            if (i/tam[0]%2 == 0):
                img[(0 + i):(tam[0] + i), (0 + j):(tam[1] + j)] = cv2.rotate(menor_frame, cv2.ROTATE_180)
            else:
                img[(0 + i):(tam[0] + i), (0 + j):(tam[1] + j)] = menor_frame
            
    
    # Maneira individual
    # img[0:menor_frame.shape[0], 0:menor_frame.shape[1]] = menor_frame
    
    
    cv2.imshow('frame',img)
    
    if cv2.waitKey(1) == ord('q'):     
        break

cap.release()
cv2.destroyAllWindows()