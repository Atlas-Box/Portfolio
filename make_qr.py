import sys, qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

url = sys.argv[1] if len(sys.argv) > 1 else "https://atlas-box.github.io/Portfolio/"
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=16, border=2)
qr.add_data(url); qr.make(fit=True)
img = qr.make_image(image_factory=StyledPilImage,
                    module_drawer=RoundedModuleDrawer(),
                    color_mask=SolidFillColorMask(back_color=(255,255,255), front_color=(7,10,16)))
img = img.resize((640,640))
img.save("assets/qr.png")
print("QR ->", url, img.size)
