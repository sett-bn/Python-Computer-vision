#تمرین زهرا بوستانی تولید 9 تصوی 100 در 100 از یک تصویر 900 در 900 با کرنل 9 در 9

import cv2
import numpy as np

def make_9image(image_path):

    original_image = cv2.imread(image_path)
    resized_image = cv2.resize(original_image, (900, 900))
    height, width, _ = resized_image.shape

    npic0 = np.zeros((100, 100, 3), dtype=np.uint8)
    npic1 = np.zeros((100, 100, 3), dtype=np.uint8)
    npic2 = np.zeros((100, 100, 3), dtype=np.uint8)
    npic3 = np.zeros((100, 100, 3), dtype=np.uint8)
    npic4 = np.zeros((100, 100, 3), dtype=np.uint8)
    npic5 = np.zeros((100, 100, 3), dtype=np.uint8)
    npic6 = np.zeros((100, 100, 3), dtype=np.uint8) 
    npic7 = np.zeros((100, 100, 3), dtype=np.uint8)
    npic8 = np.zeros((100, 100, 3), dtype=np.uint8)
    new_images = [npic0, npic1, npic2, npic3, npic4, npic5, npic6, npic7, npic8]

    stride = 9
    for j in range(0, height, stride): 
        for i in range(0, width, stride): 
            for x in range(9):

                if i + x < width:
                    pixel = resized_image[j, i + x]
                    new_images[x][j // stride, i // stride] = pixel

    for img in new_images:
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

make_9image('image.jpg')
