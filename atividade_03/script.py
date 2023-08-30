import cv2
import numpy as np

#carregando imagem
img = cv2.imread('atividade_03\img\matas.jpg')

#array
img_array = np.array(img) 

#mostrando o array de 3 dimensões
print(img_array.shape)

# colorindo de vermelho o que for verde
for row in range(img_array.shape[0]):
    for col in range(img_array.shape[1]):
        pixel = img_array[row, col]
    #colorindo se for tom de verde - lembrar que eh B G R
        if pixel[1] > 80 and pixel[0] < 140 and pixel[2] < 140:
            img_array[row, col] = [0, 0, 255]

#transformando o array em imagem
img = np.array(img_array, dtype=np.uint8)

# mostrando imagem de resultado
cv2.imshow('img', img)

# mostrando a matriz da imagem
print(np.shape(img))

# espera imagem ser fechada
cv2.waitKey(0)
