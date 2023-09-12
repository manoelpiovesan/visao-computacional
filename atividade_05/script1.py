import cv2
import numpy as np

#carregando imagens
img = cv2.imread('atividade_05\imgs\image1.jpg')

fundo = cv2.imread('atividade_05\imgs\\fundo1.jpg')

#arrays
img_array = np.array(img) 
fundo_array = np.array(fundo)

# mostrando o arrays de 3 dimensões
print(img_array.shape)
print(fundo_array.shape)

#percorrendo o array da imagem
for i in range(0, fundo_array.shape[0]):
    for j in range(0, fundo_array.shape[1]):
        #trocando por fundo se for verde
        try:
            [b, g, r] = img_array[i][j]
        except:
            continue
        # se for tom de verde 
        if g > 150 and b < 190 and r < 190:
            img_array[i][j] = fundo_array[i][j]
        

#mostrando imagem
cv2.imshow('Imagem', img_array)
cv2.waitKey(0)

