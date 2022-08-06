# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_rotate.py

# import packages yang diperlukan
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

# Mengambil dimensi gambar dan hitung pusatnya
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# Memutar gambar sebesar 45 derajat di sekitar bagian tengah gambar
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

# Memutar gambar sebesar -90 derajat di sekitar gambar
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

# Memutar gambar secara acak dari titik tingah
M = cv2.getRotationMatrix2D((10, 10), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Arbitrary Point", rotated)

# Menggunakan fungsi dari Imutils untuk memutar dari gambar
# sebesar 180 derajat
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)

# Memutar gambar sebesar 33 derajat berlawanan dengan jarum jam
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)

# Referensi: pyimagesearch