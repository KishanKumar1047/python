
# import segno
# qrcode = segno.make_qr("hello , world")
# qrcode.save("basic_qrcode.png")


import qrcode as qr 
img = qr.make("hello , everyone")
img.save("basic_hello.png")