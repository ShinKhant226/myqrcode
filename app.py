import pyqrcode 
import png 
import os
from flask import Flask,render_template,redirect,url_for,request
from pyqrcode import QRCode

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/create',methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        text = str(request.form['user_text'])
        qrcode = pyqrcode.create(text)

        location = "static"
        path = os.path.join(location,'myqr.png') 

        photo = qrcode.png('static/myqr.png', scale = 6)  
        return render_template('qr.html',photo=path)
        os.remove(path)
    else:
        return render_template('index.html')

# @app.route('/scan')
# def scan():
#    return render_template('scan.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('404.html'), 403

@app.errorhandler(410)
def page_forbidden(e):
    return render_template('404.html'), 410

if __name__ == '__main__':
   app.run(debug = True)