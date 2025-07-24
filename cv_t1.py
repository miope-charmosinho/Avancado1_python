import cv2

#modo como quero carregar a imagem (segundo argumento do parametro) existem 3 modos:
#-1, cv2.IMREAD_COLOR: lerá a imagem de maneira colorida, porém qualquer transparência não será lida
#0, cv2.IMREAD_GRAYSCALE: lerá a imagem em escalas de cinza
#1, cv2.IMREAD_UNCHANGED: carrega a imagem como ela é

try:
    img = cv2.imread('/home/igor/codes/A1_python/coisas/carta_3.jpg', 0)#importando a imagem
    img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5) #redimensionando
    #img = cv2.resize(img, (400, 800))     # redimensionando por numero de pixel
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

except:
    print('\nNão foi possivel encontrar a imagem\n')

else:
    cv2.imwrite('codes/A1_python/coisas/dandan.jpg', img) #salvar imagem manipulada como nova imagem

    cv2.imshow('Titulo foda', img)
    cv2.waitKey(0) #se voce pressionar em qualquer lugar, a janela com a imagem será fechada, 0 espera um tempo infinito
    cv2.destroyAllWindows()

# Problemas!
#   1) Não consegui rotacionar a imagem
#   2) Não consegui fazer a imagem fechar após "x" segundos

# Solução
#   1) Era só não repetir um segundo "cv2." que dava
#   2) Tá em milisegundos, eu tava colocando uns 5 milisegundos e esperando que fosse visivel a porra do bagulho
