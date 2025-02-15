import qrcode
import qrcode.constants 
from PIL import Image

#use QRcode class to change version and correct error

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=8, border=5,
)
qr.add_data('https://github.com/rajanyamuk')
qr.make(fit=True) #if true then works
img = qr.make_image(
    fill_color = "green", back_color = "white"
)
img.save("rajanya_github.png")

