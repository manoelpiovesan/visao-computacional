import cv2
import numpy as np

#carregando imagem
img = cv2.imread('atividade_04\images\Img5.jpg')

#array
img_array = np.array(img) 

#mostrando o array de 3 dimensões
print(img_array.shape)

for row in range(img_array.shape[0]):
    for col in range(img_array.shape[1]):
        pixel = img_array[row, col]

        # colorindo se for tom de amarelo
        blue, green, red = pixel
        if blue < green and blue < red and green > 140 and red > 140 and blue < 150:
            img_array[row, col] = [0, 0, 255]

        # colorindo se for tom de branco
        if blue > 210 and green > 210 and red > 210:
            img_array[row, col] = [0, 255, 0]

#transformando o array em imagem
img = np.array(img_array, dtype=np.uint8)

# mostrando imagem de resultado
cv2.imshow('img', img)

# mostrando a matriz da imagem
print(np.shape(img))

# espera imagem ser fechada
cv2.waitKey(0)
