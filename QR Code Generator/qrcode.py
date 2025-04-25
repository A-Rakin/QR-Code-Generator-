import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqrcode = qrcode.make("https://www.youtube.com/")

myqrcode.save("QrCode.png",scale = 8)


c = decode(Image.open("myqrcode.png"))
print(c[0].data.decode("ascii"))