import os
from flask import Flask, render_template, request


from ocr_core import ocr_core1, ocr_core2, ocr_core3, ocr_core4



UPLOAD_FOLDER = '/static/uploads/'


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':

        if 'file' not in request.files:
            return render_template('upload.html', msg='Ninguna imagen seleccionada')
        file = request.files['file']

        if file.filename == '':
            return render_template('upload.html', msg='Ninguna imagen seleccionada')

        if file and allowed_file(file.filename):


            extracted_text = ocr_core1(file)
            enumerate_text = ocr_core2(file)
            sevenwords_text = ocr_core3(file)
            frequent_words = ocr_core4(file)

            return render_template('upload.html',
                                   msg='Tu imagen se ha procesado con éxito!',
                                   extracted_text=extracted_text,
                                   enumerate_text=enumerate_text,
                                   sevenwords_text=sevenwords_text,
                                   frequent_words=frequent_words,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()