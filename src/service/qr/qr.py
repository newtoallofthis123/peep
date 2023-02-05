from ..format import *

class Qr:
    def __init__(self, action, query):
        self.action = action
        self.file = query.split(" ")[0]
        self.query = ' '.join(query.split(" ")[1:])

    def dir_make(self, file):
        import os
        home_dir = os.path.expanduser( '~' )
        os.mkdir(os.path.join(home_dir, ".peep")) if not os.path.exists(os.path.join(home_dir, ".peep")) else None
        os.mkdir(os.path.join(home_dir, ".peep", "qr")) if not os.path.exists(os.path.join(home_dir, ".peep", "qr")) else None
        return os.path.join(home_dir, ".peep", "qr", file)
    def qr_make(self):
        from pyqrcode import create
        c_print("Making QR Code...", code="info")
        qr = create(self.query)
        qr.png(self.dir_make(f'{self.file}.png'), scale=8)
        c_print("QR Code Made Successfully!", code="success")
        c_print(f"QR Can be found at: {self.dir_make(f'{self.file}.png')}", code="info")
        open_response = ask(f"Do you want to open {self.file}.png?")
        if open_response:
            from ..brain import platform
            import os
            if platform() == "win":
                os.system(f"start {self.dir_make(f'{self.file}.png')}")
            else:
                os.system(f"open {self.dir_make(f'{self.file}.png')}")
    def make(self):
        from pyqrcode import create
        if self.action == "make":
            c_print("Making QR Code...", code="info")
            qr = create(self.query)
            qr.png(self.dir_make(f'{self.file}.png'), scale=8)
            c_print("QR Code Made Successfully!", code="success")
            c_print(f"QR Can be found at: {self.dir_make(f'{self.file}.png')}", code="info")
            open_response = ask(f"Do you want to open {self.file}.png?")
            if open_response:
                from ..brain import platform
                import os
                if platform() == "win":
                    os.system(f"start {self.dir_make(f'{self.file}.png')}")
                else:
                    os.system(f"open {self.dir_make(f'{self.file}.png')}")
        elif self.action == "read":
            c_print("Reading QR Code...", code="info")
            from pyzbar.pyzbar import decode
            from PIL import Image
            img = Image.open(self.dir_make(f'{self.file}.png'))
            code = decode(img)
            c_print(f"QR Code Data:", code="normal")
            c_print(f"{code[0].data.decode('utf-8')}", code="success")
        elif self.action == "open":
            from ..brain import platform
            import os
            if platform() == "win":
                os.system(f"start {self.dir_make(f'{self.file}.png')}")
            else:
                os.system(f"open {self.dir_make(f'{self.file}.png')}")
        elif self.action == "list":
            import os
            c_print(f"Listing QR Codes in {self.dir_make('')}...", code="info")
            with os.scandir(self.dir_make("")) as entries:
                for entry in entries:
                    print(entry.name)
        elif self.action == "delete":
            import os
            c_print(f"Deleting {self.file}.png...", code="info")
            if os.path.exists(self.dir_make(f'{self.file}.png')):
                os.remove(self.dir_make(f'{self.file}.png'))
                c_print(f"Deleted {self.file}.png", code="success")
            else:
                c_print(f"{self.file}.png Not Found", code="danger")
        else:
            c_print("Invalid Action", code="danger")

    def img_qr(self):
        import segno
        import os
        qrcode = segno.make(self.query, error='h')
        bg = self.action
        if os.path.exists(os.path.join(os.getcwd(), bg)):
            qrcode.to_artistic(background=bg, target=self.dir_make(f'{self.file}.png'), scale=10)
            c_print("QR Code Made Successfully!", code="success")
            c_print(f"QR Can be found at: {self.dir_make(f'{self.file}.png')}", code="info")
            return True
        else:
            c_print("Background Image Not Found", code="danger")
            qr_response = ask("Do you want to make a normal QR Code Instead?")
            if qr_response:
                self.qr_make()
                return True
            else:
                c_print("Okay...", code="info")
            return False