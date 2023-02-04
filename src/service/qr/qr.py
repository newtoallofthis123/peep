from ..format import *

class Qr:
    def __init__(self, action, query):
        self.action = action
        self.file = query.split(" ")[0]
        self.query = ' '.join(query.split(" ")[1:])

    def make(self):
        from pyqrcode import create
        if self.action == "make":
            c_print("Making QR Code...", code="info")
            qr = create(self.query)
            qr.png(f'{self.file}.png', scale=8)
            c_print("QR Code Made Successfully!", code="success")
            open_response = ask(f"Do you want to open {self.file}.png?")
            if open_response:
                from ..brain import platform
                import os
                if platform() == "win":
                    os.system(f"start {self.file}.png")
                else:
                    os.system(f"open {self.file}.png")
        elif self.action == "read":
            c_print("Reading QR Code...", code="info")
            from pyzbar.pyzbar import decode
            from PIL import Image
            img = Image.open(self.file)
            code = decode(img)
            c_print(f"QR Code Data:", code="normal")
            c_print(f"{code[0].data.decode('utf-8')}", code="success")
        else:
            c_print("Invalid Action", code="danger")