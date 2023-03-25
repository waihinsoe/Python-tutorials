import qrcode
import image
qr = qrcode.QRCode(
    version =1 ,
    box_size = 15,
    border = 5
)

data = 'https://www.wahinsoe.com/list/home'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color = 'white')
img.save('YouTube Channel QR Code.png')