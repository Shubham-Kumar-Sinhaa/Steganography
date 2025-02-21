import cv2
import os
import string

img = cv2.imread("encryptedImage.jpg")

with open("password.txt","r") as passfile:
    password = passfile.read().strip()

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(255*2):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")