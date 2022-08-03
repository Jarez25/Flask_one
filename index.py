from distutils.log import debug
from tkinter import TRUE
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros ():
    return render_template('sobre_nosotros.html')

if __name__ == '__main__':
    app.run(debug=True)