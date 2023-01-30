from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from reader_txt_ import *
from database import *
import os

UPLOAD_FOLDER = './temp'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route('/result', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], "CNAB.txt"))
      read()
      result = databaseFatch()
      return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)