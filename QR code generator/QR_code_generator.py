# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

def generate_qr_code(url):
    # String which represents the QR code url link
    url = ""
    
    # Generate QR code
    url_encoded = pyqrcode.create(url)
    
    # Create and save the qr code in both svg and png file
    url_encoded.svg("qr_code.svg", scale = 8)
    url_encoded.png('qr_code.png', scale = 6)
    return

if __name__=="__main__":
    genrate_qr_code("https://docs.python.org/3/")