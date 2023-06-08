# Take a link from user and make it into a qrcode and save it on the device.

import qrcode
link = input("Enter the link to convert to QR: ")
name = input("Enter the name for the QR: ")
qr = qrcode.make(link)
qr.save(f"{name}.png")