import numpy as np
import cv2

img = cv2.imread('/home/igor/codes/A1_python/coisas/Lebron.jpg', 0)
ball = cv2.imread('/home/igor/codes/A1_python/coisas/LeBall.jpg', 0)

h, w = ball.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for meth in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, ball, meth)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if meth in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 4)
    cv2.imshow('procura', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Esse método pega nosso "template" e testa ele em todas as localizações possiveis da imagem 

# img: [[255,255,255,255],      template: [[100,100],      resultado: [[0.25, 0.50, 0.25],
#       [255,100,100,255],                 [100,100]]                  [0.50, 1.00, 0.50],
#       [255,100,100,255],                                             [0.25, 0.50, 0.25]]
#       [255,255,255,255]]

# Com isso, conseguimos uma matriz de tamanho (W-w+1, H-h+1) que mostra o quanto o templete se encaixou na imagem testada
