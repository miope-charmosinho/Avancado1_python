import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    alt = frame.shape[0]
    comp = frame.shape[1]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([140, 255, 255])

    mascara_a = cv2.inRange(hsv, lower_blue, upper_blue)

    so_a = cv2.bitwise_and(frame, frame, mask=mascara_a)

    cv2.imshow('Uau', so_a)
    cv2.imshow('mascara', mascara_a)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Pelo visto os limites do ".inRange()" não são BGR são HSV
# HSV:
#   Hue) Cor, de 0 à 179 (devia ser 360?)
#   Saturation) Saturação, de 0 à 255
#   Value) Brilho, de 0 à 255

# Sinceramente, vale mais a pena não usar esse sistema, ou pesquisar na internet códigos parecidos