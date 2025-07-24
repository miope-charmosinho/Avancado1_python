import numpy as np
import cv2

res = cv2.resize(cv2.imread('/home/igor/codes/A1_python/coisas/ryu1.jpg', -1), (0,0), fx = 0.5, fy = 0.5)

cinza = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
median_blur = cv2.medianBlur(cinza, 7)

cantos = cv2.goodFeaturesToTrack(median_blur, 2000, 0.01, 5)      # imagem / quantos pontos / qualidade de ponto / espaço minimo entre pontos
cantos = np.int32(cantos)       # O homem to tutorial usou int0, simplesmente não achei esse cara

coords = []

for cant in cantos:
    x, y = cant.ravel()
    lis = (int(x), int(y))
    cv2.circle(res, (x, y), 3, (0,255,0), -1)
    coords.append(lis)


# Condição de teste
if 1 == 0:
    for i in range(1, len(cantos)):
        cor = np.random.randint(0,255, size = 3)
        Rcor = (int(cor[0]), int(cor[1]), int(cor[2]))
        cv2.line(res, coords[i-1], coords[i], Rcor, 1)
# Fiz com que cada ponto estivesse ligado ao ponto anterior e o seguinte
# Claramente o método shi-tomasi não tem uma ordem clara de escolha de pontos


# Condição de teste
if 1 == 1:
    for i in range(1, len(cantos)):
        for j in range(i, len(cantos)):
            if ((((float(coords[i][0]) - float(coords[j][0]))**2.0)**0.5) <= 25) and ((((float(coords[i][1]) - float(coords[j][1]))**2.0)**0.5) <= 25):
                cv2.line(res, coords[j], coords[i], (0,255,0), 1)
# Testei a distância entre cada ponto e desenhei uma linha
# Melhor contorno, porém mais lento e ainda cheio de falhas

cv2.imshow('STF', median_blur)
cv2.imshow('Supremo Tribunal Federal', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

