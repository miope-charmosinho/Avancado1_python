import numpy as np
import cv2

img = cv2.resize(cv2.imread('/home/igor/codes/A1_python/coisas/Nago.jpg', -1), (0,0), fx= 0.5, fy= 0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, trash0 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
ret, trash1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, trash2 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret, trash3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
ret, trash4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

Tr = [trash0, trash1, trash2, trash3, trash4]

cv2.imshow('Nago',  img)
for i in range(0, len(Tr)):
    cv2.imshow('Trash', Tr[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()