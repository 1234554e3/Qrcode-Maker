import qrcode

img = qrcode.make("https://www.instagram.com/rohitbedse_/")

img.save("myQrcode.png")
img.show()
