#تمرین  نیوز ریداکش زهرا بوستانی
import cv2 as cv
import numpy as np
import random as rnd
import math

# Image path
img_path = "1.jpg"
img_original = cv.imread(img_path)
img_with_noise = img_original.copy()
img_denoised = img_original.copy()
width = img_original.shape[1]
height = img_original.shape[0]

# Noise percentage
noise_percent = float(input("Enter a percent of noise to apply: "))

def add_uniform_noise(image, width, height, noise_percent):
    num_noisy_pixels = int(width * height * noise_percent / 100)
    
    for _ in range(num_noisy_pixels):
        y = rnd.randint(0, height - 1)
        x = rnd.randint(0, width - 1)
        noise_value = rnd.randint(0, 255)
        image[y, x] = [noise_value, noise_value, noise_value]

    return image

noisy_image = add_uniform_noise(img_with_noise, width, height, noise_percent)

def is_extreme(pixel):
    return (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0) or (pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255)

def get_neighbors(image, y, x, channel):
    neighbors = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            if 0 <= y + dy < image.shape[0] and 0 <= x + dx < image.shape[1]:
                neighbors.append(image[y + dy, x + dx, channel])
    return neighbors

def filter_pixels(neighbors):
    return [val for val in neighbors if val != 0 and val != 255]

for y in range(1, height - 1):
    for x in range(1, width - 1):
        pixel_value = noisy_image[y, x]

        if is_extreme(pixel_value):
            red_neighbors = get_neighbors(noisy_image, y, x, 2)
            green_neighbors = get_neighbors(noisy_image, y, x, 1)
            blue_neighbors = get_neighbors(noisy_image, y, x, 0)

            true_red = filter_pixels(red_neighbors)
            true_green = filter_pixels(green_neighbors)
            true_blue = filter_pixels(blue_neighbors)

            if len(true_red) == 0 or len(true_green) == 0 or len(true_blue) == 0:
                new_r = 0 
                new_g = 0 
                new_b = 0
              
            elif len(true_red) == 1 or len(true_green) == 1 or len(true_blue) == 1:
                new_r = true_red[0] 
                new_g = true_green[0] 
                new_b = true_blue[0]
              
            else:
                new_r = math.floor(np.median(true_red))
                new_g = math.floor(np.median(true_green))
                new_b = math.floor(np.median(true_blue))

            img_denoised[y, x] = [new_b, new_g, new_r]

# Display images
cv.imshow("Original Image", img_original)
cv.imshow("Noisy Image", noisy_image)
cv.imshow("Denoised Image", img_denoised)
cv.waitKey(0)
cv.destroyAllWindows()
