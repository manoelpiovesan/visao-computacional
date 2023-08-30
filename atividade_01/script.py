import cv2
import numpy as np

#carregando imagem
img = cv2.imread('atividade_01\img\people2.jpg')

#desenhando retângulos ao redor da face das pessoas
cv2.rectangle(img, (490, 190), (700, 520), (255, 0, 0), 3)
cv2.rectangle(img, (880, 190), (1070, 460), (255, 0, 0), 3)
cv2.rectangle(img, (1340, 190), (1540, 460), (255, 0, 0), 3)

# mostrando imagem de resultado
cv2.imshow('img', img)

# mostrando a matriz da imagem
print(np.shape(img))

# espera imagem ser fechada
cv2.waitKey(0)
