# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_masking.py

# import packages yang diperlukan
import numpy as np
import argparse
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="kindo.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

# Memuat/me-load gambar dan menampilkannya ke layar
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Membuat mask berukuran sama dengan gambar, namun hanya menggunakan
# 2 nilai piksel yaitu 0 dan 255 -- latar belakang diabaikan dan diberi nilai
# 0 piksel, sedangkan objek pada gambar diberi nilai 255
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (100, 30), (400, 450), 255, -1) # (-x,y) (x,-y)
cv2.imshow("Rectangular Mask", mask)

# Menerapkan mask yang digabungkan dengan objek gambar
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# now, let's make a circular mask with a radius of 100 pixels and
# apply the mask again

# Sekarang membuat mask berbentuk lingkaran,
# dengan radius 100 piksel dan menerapkan mask
# pada gambar seperti sebelumnya
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (145, 200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)

# tampilkan gambar keluaran
cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Referensi: pyimagesearch