# تمرین زهرا بوستانی بینایی مشین زوم تصویر
import cv2

def zoom(img, number):
    darsad = number / 100.0

    if darsad != 0:
        new_dim = (int(img.shape[1] * (1 + darsad)), int(img.shape[0] * (1 + darsad)))
        zoom_image = cv2.resize(img, new_dim, interpolation=cv2.INTER_LINEAR)
    else:
        zoom_image = img

    cx, cy = zoom_image.shape[1] // 2, zoom_image.shape[0] // 2
    orig_cx, orig_cy = img.shape[1] // 2, img.shape[0] // 2

    x1 = max(0, cx - orig_cx)
    y1 = max(0, cy - orig_cy)
    x2 = min(zoom_image.shape[1], cx + orig_cx)
    y2 = min(zoom_image.shape[0], cy + orig_cy)

    cropped_img = zoom_image[y1:y2, x1:x2]

    cv2.imshow('Modified Image', cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_path = r"C:\Users\Setare\Desktop\images.jpg"
img = cv2.imread(img_path)

number = int(input("Enter number: "))
zoom(img, number)
