from flask import Flask, render_template, url_for, request
# from werkzeug.utils import secure_filename
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

    os.system("python ../yolov5/detect.py --weights ../best.pt --img 360 --conf 0.40 --source res/original/img2.jpg")

    species_type = select_web()

    if(species_type == "marble_catfish"):
        return render_template('marble_catfish.html')
    elif(species_type == "giant_african_snail"):
        return render_template('giant_african_snail.html')
    elif(species_type == "clown_knifefish"):
        return render_template('clown_knifefish.html')
    elif(species_type == "apple_snail"):
        return render_template('apple_snail.html')
    elif(species_type == "rainbow_trouty"):
        return render_template('rainbow_trouty.html')
    elif(species_type == "scavenger"):
        return render_template('scavenger.html')
    elif(species_type == "red_eared_slider"):
        return render_template('red_eared_slider.html')
    else:
        return render_template('index.html')

def select_web():
    file = open('res/detected.txt', 'r')
    data = file.read().splitlines()
    file.close()

    return data[len(data)-1].split(' ')[0]

if(__name__=="__main__"):
    app.run(debug=False)