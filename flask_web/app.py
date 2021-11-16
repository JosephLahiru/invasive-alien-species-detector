from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
import cv2, numpy, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    npimg = numpy.fromfile(request.files['pic'], numpy.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    cv2.imwrite("res/original/img2.jpg", img)

    os.system("python ../yolov5/detect.py --weights ../best.pt --img 360 --conf 0.25 --source res/original/img2.jpg")

    return render_template('index.html')

    #filename = secure_filename(pic.filename)

if(__name__=="__main__"):
    app.run(debug=True)