# Cara penggunaan, ketik perintah berikut pada terminal👇
# python load_image_opencv.py --image kodingindonesia.jpg

# import packages yang diperlukan
import argparse
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# Memuat/me-load gambar dari disk melalui "cv2.imread" dan kemudian ambil spasial
# dimensions, including width, height, and number of channels
image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

# Tunjukkan gambar dan tunggu penekanan tombol
cv2.imshow("Image", image)
cv2.waitKey(0)

# Tampilkan lebar gambar, tinggi, dan jumlah channels
# melalui terimal/cmd
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# Referensi: pyimagesearch</pre>