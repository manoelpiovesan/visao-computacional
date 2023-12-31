import cv2
import numpy as np

#carregando imagem
img = cv2.imread('atividade_02\img\people2.jpg')

#desenhando retângulos ao redor da face das pessoas
cv2.rectangle(img, (490, 190), (700, 520), (255, 0, 0), 3)
cv2.rectangle(img, (880, 190), (1070, 460), (255, 0, 0), 3)
cv2.rectangle(img, (1340, 190), (1540, 460), (255, 0, 0), 3)

#escrevendo texto abaixo dos retângulos das faces
cv2.putText(img, 'Pessoa 1', (520, 560), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Pessoa 2', (910, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Pessoa 3', (1370, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# mostrando imagem de resultado
cv2.imshow('img', img)

# mostrando a matriz da imagem
print(np.shape(img))

# espera imagem ser fechada
cv2.waitKey(0)
