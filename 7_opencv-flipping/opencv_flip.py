# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_flip.py

# import packages yang diperlukan
import argparse
import cv2

# Membuat parser argumen dan parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

# Memuat/me-load gambar dan menampilkannya ke layar
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Putar gambar secara horizontal
print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

# Putar gambar secara vertikal
flipped = cv2.flip(image, 0)
print("[INFO] flipping image vertically...")
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

# Memutar gambar secara vertikal dan horizontal
flipped = cv2.flip(image, -1)
print("[INFO] flipping image horizontally and vertically...")
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

# Referensi: pyimagesearch