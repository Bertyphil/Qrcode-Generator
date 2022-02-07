import qrcode 
img = qrcode.make("Hi testing!")
img.save("QRcode\myqrcode.jpg")