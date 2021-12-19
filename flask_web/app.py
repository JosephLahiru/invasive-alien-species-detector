from flask import Flask, render_template, url_for, request
# from werkzeug.utils import secure_filename
import cv2, numpy, os, random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/process_data", methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':
        if request.form.get('launch_plant') == 'Launch Plant':
            return render_template('process_plant.html')
        elif request.form.get('launch_animal') == 'Launch Animal':
            return render_template('process_animal.html')

@app.route('/upload_ani', methods=['POST'])
def upload_ani():

    npimg = numpy.fromfile(request.files['pic'], numpy.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    cv2.imwrite("res/original/img2.jpg", img)

    os.system("python3 ../yolov5/detect.py --weights ../models/animal_model.pt --img 360 --conf 0.40 --source res/original/img2.jpg")

    # species_type = select_web("animal")
    species_type = select_web()

    print(f"Found a {species_type}")

    if(species_type == "marble_catfish"):
        return render_template('animals/marbel_catfish.html')
    elif(species_type == "giant_african_snail"):
        return render_template('animals/giant_african_snail.html')
    elif(species_type == "clown_knifefish"):
        return render_template('animals/clown_knifefish.html')
    elif(species_type == "apple_snail"):
        return render_template('animals/apple_snail.html')
    elif(species_type == "rainbow_trouty"):
        return render_template('animals/rainbow_trout.html')
    elif(species_type == "scavenger"):
        return render_template('animals/scavenger.html')
    elif(species_type == "red_eared_slider"):
        return render_template('animals/red_eared_slider.html')
    else:
        return render_template('index.html')

@app.route('/upload_plant', methods=['POST'])
def upload_plant():

    npimg = numpy.fromfile(request.files['pic'], numpy.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    cv2.imwrite("res/original/img2.jpg", img)

    os.system("python3 ../yolov5/detect.py --weights ../models/plant_model.pt --img 360 --conf 0.40 --source res/original/img2.jpg")

    # species_type = select_web("plant")
    species_type = select_web()

    print(f"Found a {species_type}")

    if(species_type == "lantana"):
        return render_template('plants/lantana.html')
    elif(species_type == "sphagneticola_trilobata"):
        return render_template('plants/sphagneticola_trilobata.html')
    elif(species_type == "clusia_rosea"):
        return render_template('plants/clusia_rosea.html')
    elif(species_type == "opuntia_dillenii"):
        return render_template('plants/opuntia_dillenii.html')
    elif(species_type == "mimosa_pigra"):
        return render_template('plants/mimosa_pigra.html')
    elif(species_type == "parthenium_hysterophorus"):
        return render_template('plants/parthenium_hysterophorus.html')
    elif(species_type == "clidemia_hirta"):
        return render_template('plants/clidemia_hirta.html')
    elif(species_type == "leucaena_leucocephala"):
        return render_template('plants/leucaena_leucocephala.html')
    elif(species_type == "alstonia_macrophylla"):
        return render_template('plants/alstonia_macrophylla.html')
    elif(species_type == "cuscuta_campestris_yunck"):
        return render_template('plants/cuscuta_campestris_yunck.html')
    elif(species_type == "dillenia_suffruticosa"):
        return render_template('plants/dillenia_suffruticosa.html')
    elif(species_type == "austroeupatorium_inulifolium"):
        return render_template('plants/austroeupatorium_inulifolium.html')
    elif(species_type == "annona_glabra"):
        return render_template('plants/annona_glabra.html')
    elif(species_type == "eichhornia_crassipes"):
        return render_template('plants/eichhornia_crassipes.html')
    elif(species_type == "panicum_maximum"):
        return render_template('plants/panicum_maximum.html')
    elif(species_type == "salvinia_molesta"):
        return render_template('plants/salvinia_molesta.html')
    elif(species_type == "prosopis_juliflora"):
        return render_template('plants/prosopis_juliflora.html')
    else:
        return render_template('index.html')

# <<<<<<< HEAD
# def select_web(type):
#     if(type == "animal"):
#         types = ["marble_catfish", "giant_african_snail", "clown_knifefish", "apple_snail",
#         "rainbow_trouty", "scavenger", "red_eared_slider"]
#     else:
#         types = ["lantana","sphagneticola_trilobata","clusia_rosea","opuntia_dillenii","mimosa_pigra",
#         "parthenium_hysterophorus","clidemia_hirta","leucaena_leucocephala","alstonia_macrophylla",
#         "cuscuta_campestris_yunck","dillenia_suffruticosa","austroeupatorium_inulifolium","annona_glabra",
#         "eichhornia_crassipes","panicum_maximum","salvinia_molesta","prosopis_juliflora"]
        
#     # file = open('res/detected.txt', 'r')
#     # data = file.read().splitlines()
#     # file.close()
# =======

@app.route('/debug', methods=['POST'])
def debug():
    return render_template("plants/lantana.html")

def select_web():
    # types = ["marble_catfish", "giant_african_snail", "clown_knifefish", "apple_snail",
    # "rainbow_trouty", "scavenger", "red_eared_slider"]
    file = open('res/detected.txt', 'r')
    data = file.read().splitlines()
    file.close()
# >>>>>>> AI_test_branch

    return data[len(data)-1].split(' ')[0]
    #return types[random.randint(0, 8)]

if(__name__=="__main__"):
    app.run(debug=True)