# Cara penggunaan, ketik perintah berikut pada terminal👇
# python image_drawing.py

# import packages yang diperlukan
import argparse
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="kindo.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

# Memuat/me-load gambar dari disk
image = cv2.imread(args["image"])

# membuat lingkaran pada wajah, menutup kedua mata dengan lingkaran,
# dam persegi panjang yang menutupi mulut
cv2.circle(image, (250, 130), 60, (0, 0, 255), 2)
cv2.circle(image, (222, 120), 10, (0, 0, 255), -1)
cv2.circle(image, (274, 120), 10, (0, 0, 255), -1)
cv2.rectangle(image, (220, 170), (280, 150), (0, 0, 255), -1)

# menampilkan output gambar ke layar
cv2.imshow("Output", image)
cv2.waitKey(0)

# Referensi: pyimagesearch