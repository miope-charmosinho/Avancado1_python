import cv2
import numpy

img = cv2.imread('/home/igor/codes/A1_python/coisas/new_war.jpg', -1)
img = cv2.resize(img, (0,0), fx = 0.25, fy = 0.25)


# Toda imagem é, na verdade, uma matriz numpy de pixels e toda ação que fazemos é uma modificação nessa matriz
# Exemplo de imagem:
# Diagonal principal de pixels pretos e a outra de pixels brancos
    # [
    # [[0,0,0], [255,255,255]],
    # [[255,255,255], [0,0,0]]
    # ]
# No cv2, as cores seguem uma paleta BGR (blue,green,red), então [255,0,0] seria um pixel completamente azul

# (540, 960, 3)
s = img.shape       # ".shape" mostra quantas linhas, colunas e tipos tem na imagem 
#print(img)      # mostra a matriz que compoe a imagem (essa aqui é muito grande)

# Trocando a cor de um quadradado de pixels
for i in range(100, 200):
    for j in range(0,s[1]):
        img[i][j] = [0,0,0]

# Mexendo na imagem usando uma parte dela mesma
circ = img[200:250, 350:400]
for j in range(0,950,50):
    img[0:50, (0 + j):(50 + j)] = circ

cv2.imwrite('codes/A1_python/coisas/war2.jpg', img)
cv2.imshow('Titulo pica', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

