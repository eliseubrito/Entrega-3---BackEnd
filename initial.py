from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from reader_txt_ import *
from database import *

UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = set('txt')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route('/result', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename("CNAB.txt"))
      read()
      result = databaseFatch()
      return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)