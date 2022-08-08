# Cara penggunaan, ketik perintah berikut pada terminal👇
# python image_arithmetic.py

# import packages yang diperlukan
import numpy as np
import argparse
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="grand_canyon.png",
	help="path to the input image")
args = vars(ap.parse_args())

# Berikut merupakan array NumPy yang disimpan sebagai bilangan bulat
# unsigned integer 8-bit(unit8) dengan nilai kisaran [0, 255];
# saat menggunakan fungsi add/subtract di OpenCV, nilai-nilai td akan
# "dipotong" atau dibatasi pada rentang [0,255] saja,
# bahkan setelah penerapan operasi tersebut.
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print("max of 255: {}".format(added))
print("min of 0: {}".format(subtracted))

# Menggunakan operasi aritmatika NumPy akan menghasilkan
# modulo ("pembungkus"), ini agar nilai tidak
# terpotong ke kisaran [0, 255] saja seperti contoh di atas
added = np.uint8([200]) + np.uint8([100])
subtracted = np.uint8([50]) - np.uint8([100])
print("wrap around: {}".format(added))
print("wrap around: {}".format(subtracted))

# Memuat/me-load gambar asli dan menampilkannya ke layar
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Meningkatkan intensitas piksel pada gambar input sebesar 100
# dilakukan dengan membuat array NumPy yang memiliki *dimensi yang sama*
# dengan gambar input, mengisinya dengan satu, mengalikannya dengan 100,
# lalu menambahkan gambar input dan matriks bersama-sama
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Lighter", added)

# lakukan hal yg sama, namun disini kita mengurangi 50 dari semua piksel
# di gambar dan membuatnya lebih gelap
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)
cv2.waitKey(0)

# Referensi: pyimagesearch