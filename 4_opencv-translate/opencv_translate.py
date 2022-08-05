# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_translate.py

# import packages yang diperlukan
import numpy as np
import argparse
import imutils
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

# Memuat/me-load gambar dan menampilkannya ke layar
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Geser gambar sebanyak 25 piksel ke kanan dan 50 piksel ke bawah
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

# Sekarang geser gambar sebanyak 50 piksel ke kiri dan 90 piksel
# ke atas dengan menentukan masing-masing nilai negatif untuk arah x dan y
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# Menggunakan fungsi dari Imutils untuk menerjemakan gambar 100 piksel
# ke bawah dalam satu panggilan funsgi
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)