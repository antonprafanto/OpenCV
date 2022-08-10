# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_channels.py

# import packages yang diperlukan
import numpy as np
import argparse
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

# Memuat/me-load gambar dan menampilkannya ke layar,
# serta simpan channel warna yg direpresentasikan sebagai
# array NumPy yg memiliki urutan Blue, Green, Red
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

# Menampilkan masing-masing channel secara terpisah
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# Gabungkan gambar yg sebelumnya terpisah
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Visualisasikan setiap channel dalam warna
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)