# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_getting_setting.py

# import packages yang diperlukan
import argparse
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="ai.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

# Memuat/me-load gambar, kemudian ambil spasial dimensions (width and height),
# dan kemudian tampilkan gambar asli ke layar
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# Gambar hanyalah array NumPy -- dengan titik asal (0, 0) terletak di
# kiri atas gambar
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Mengakses piksel yang terletak di x=50, y=20
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Perbarui piksel di (50, 20) dan atur ke merah
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.waitKey(0)

# Referensi: pyimagesearch