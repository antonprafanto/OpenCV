# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_resize.py

# import packages yang diperlukan
import argparse

# install imutils 👉 pip install imutils
import imutils
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="kindo.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

# Memuat/me-load gambar dan menampilkannya ke layar
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Merubah ukuran lebar gambar menjadi 150 piksel,
# tapi untuk mencegah gambar menjadi miring/distorsi, pertama-tama kita
# harus menghitung rasio lebar baru dengan lebar lama
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# Melakukan pengubahan ukuran gambar yang sebenarnya
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

# Merubah ukuran tinggi gambar sebesar 50 piksel dengan
# memperhitungkan aspek rasio gambar
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

# Melakukan pengubahan ukuran gambar yang sebenarnya
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# calculating the ratio each and every time we want to resize an
# image is a real pain, so let's use the imutils convenience
# function which will *automatically* maintain our aspect ratio
# for us

# Menghitung rasio setiap kali kita ingin mengubah ukuran gambar
# sangat merepotkan, jadi mari kita gunakan fungsi Imutils
# yang akan *secara otomatis* menjaga aspek rasio
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)

# Membuat daftar metode interpolasi di OpenCV
methods = [
	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
	("cv2.INTER_AREA", cv2.INTER_AREA),
	("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

# Ulangi metode interpolasi
for (name, method) in methods:
	#tingkatkan ukuran gambar sebanyak 3x menggunakan metode
	# interpolasi saat ini
	print("[INFO] {}".format(name))
	resized = imutils.resize(image, width=image.shape[1] * 3,
		inter=method)
	cv2.imshow("Method: {}".format(name), resized)
	cv2.waitKey(0)

	# Referensi: pyimagesearch