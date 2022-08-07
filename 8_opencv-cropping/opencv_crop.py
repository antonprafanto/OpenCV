# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_crop.py

# import packages yang diperlukan
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

# Image Cropping dengan OpenCV dilakukan melalui irisan array Numpy
# sederhana dengan urutan startY:endY, startX:endX - di sini kita memotong
# wajah dari gambar (koordinat ini ditentukan menggunakan perangkat
# lunak pengedit foto seperti Photoshop, GIMP, Paint, dll. .)
face = image[40:200, 170:320]
cv2.imshow("Face", face)
cv2.waitKey(0)

# Menerapkan image cropping lain, kali ini mengekstrak gambar badan
body = image[200:550, 100:400]
cv2.imshow("Body", body)
cv2.waitKey(0)

# Referensi: pyimagesearch