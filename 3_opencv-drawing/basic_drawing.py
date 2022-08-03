# Cara penggunaan, ketik perintah berikut pada terminal👇
# python basic_drawing.py

# import packages yang diperlukan
import numpy as np
import cv2

# inisialisasi kanvas dengan ukuran gambar 300 x 300 piksel menggunakan 3 channel
# (Red, Green, and Blue) dengan background hitam
canvas = np.zeros((300, 300, 3), dtype="uint8")

# menggambar garis hijau dari kiri-atas ke ujung kanan-bawah kanvas
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas 1", canvas)
# cv2.waitKey(0)

# menggambar garis tebal merah berukuran 3 piksel
# dari kanan-atas ke ujung kiri-bawah
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas 2", canvas)
# cv2.waitKey(0)

# menggambar kotak hijau berukuran 50x50 piksel,
# dimulai dari 10x10 dan berakhir di 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas 3", canvas)
# cv2.waitKey(0)

# menggambar persegi panjang lainnya, berwarna merah
# dan memiliki ketebalan 5 piksel
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas 4", canvas)
# cv2.waitKey(0)

# menggambar persegi panjang terakhir yg diisi warna biru
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas 5", canvas)
# cv2.waitKey(0)

# inisialisasi ulang kanvas sebagai array yg kosong, kemudian
# hitung pusat koordinat (x, y) kanvas
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# melakukan looping menambahkan ukuran radius, dari 25 piksel to 150 piksel
# dengan kelipatan 25 piksel
for r in range(0, 175, 25):
	# menggambar lingkarang putih dengan ukuran radius terkini
	cv2.circle(canvas, (centerX, centerY), r, white)

# menampilkan kanvas pada layar
cv2.imshow("Canvas 6", canvas)
# cv2.waitKey(0)

# inisialisasi ulang kanvas
canvas = np.zeros((300, 300, 3), dtype="uint8")

# let's draw 25 random circles
# mulai menggambar 25 lingkaran secara acak
for i in range(0, 25):
	# generate ukuran radius secara acak antara 5 dan 200, generate warna
	# secara acak, dan kemudian pilih titik secara acak pada kanvas
	# dimana lingkaran akan digambar
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size=(3,)).tolist()
	pt = np.random.randint(0, high=300, size=(2,))

	# menggambar lingkaran secara acak pada kanvas
	cv2.circle(canvas, tuple(pt), radius, color, -1)

# menampilkan 'mastespiece' ke layar
cv2.imshow("Canvas 7", canvas)
cv2.waitKey(0)

# Referensi: pyimagesearch