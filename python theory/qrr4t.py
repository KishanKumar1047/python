import segno

# Data to be encoded
data = "https://wa.me/qr/5LXYCW5BUBFAA1"

# Create a QR Code
qr = segno.make(data)

# Save the QR Code as an image file
qr.save("qrcode.png")

# Optionally, you can save it in other formats like SVG, PDF, etc.
qr.save("qrcode.svg")
