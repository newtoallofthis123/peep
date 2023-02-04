class Ui:
    def __init__(self, url, info):
        self.url = url
        self.info = info

    def server(self):
        from flask import Flask, render_template
        app = Flask(__name__)
        @app.route('/')
        def index():
            return render_template('index.html', stream=self.url, info=self.info)
        app.run()