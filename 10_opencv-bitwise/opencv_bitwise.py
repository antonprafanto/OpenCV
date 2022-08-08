# Cara penggunaan, ketik perintah berikut pada terminal👇
# python opencv_bitwise.py

# import packages yang diperlukan
import numpy as np
import cv2

# Menggambar persegi panjang
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# Menggambar lingkaran
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)


# Jika operasi logika biner (bitwise) 'AND' hanya bernilai 'True'
# ketika kedua input memiliki nilai "ON" -- dalam hal
# ini, fungsi cv2.bitwise_and memeriksa setiap piksel dalam
# persegi panjang dan lingkaran; jika *Kedua* piksel memiliki nilai
# lebih besar dari nol (beririsam) maka piksel menjadi 'ON (yaitu, 255)
# pada gambar output; jika hanya salah satu saja,
# nilai output diatur ke 'OFF' (yaitu, 0)
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# bitwise 'ATAU' memeriksa setiap piksel dalam dua input,
# dan jika *Salah Satu* piksel dalam persegi panjang atau
# lingkaran lebih besar dari nol, maka piksel
# keluaran memiliki nilai 255, selain itu adalah 0
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# bitwise 'XOR' identik dengan fungsi 'ATAU',
# dengan satu pengecualian: baik persegi panjang dan lingkaran
# tidak boleh *Kedua*-nya memiliki nilai lebih besar dari 0
# (hanya satu yang bisa 0)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# bitwise 'NOT' membalikkan nilai piksel;
# piksel dengan nilai 255 menjadi 0,
# dan piksel dengan nilai 0 menjadi 255
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

# Referensi: pyimagesearch