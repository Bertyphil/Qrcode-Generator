import cv2
d = cv2.QRCodeDetector()
image = cv2.imread("QRcode\myqrcode.jpg")
	
a = d.detectAndDecode(image) #returns a list
print("Decoded text is: ",a[0])