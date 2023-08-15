import qrcode

img = qrcode.make("Enter Your Link Here")

img.save("myQrcode.png")
img.show()
