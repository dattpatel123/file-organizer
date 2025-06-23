import os
from flask import Flask, render_template, request, redirect, send_file
from flask_dropzone import Dropzone
import functions
import shutil




app = Flask(__name__)
dropzone = Dropzone(app)

basedir = os.path.abspath(os.path.dirname(__file__))
uploadsPath = os.path.join(basedir, 'uploads')

# Main Page w/ Dropzone

@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template('index.html')

# Upload File Route
@app.route('/uploadFiles', methods=['POST'])
def uploadFiles():
    
    if not os.path.exists(uploadsPath):
        os.mkdir(uploadsPath)

    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(uploadsPath, f.filename))
    
    return 'uploaded'


#Organize Dropped Files

@app.route('/result', methods=['GET'])
def result():
    
    # if no file uploaded
    if not os.path.isdir(uploadsPath) or len(os.listdir(uploadsPath)) == 0:
        return render_template('empty.html')
    
    # organize files then give categories and counts
    functions.organize()
    functions.findCounts()

    # Make the zip file and delete files from local storage
    shutil.make_archive('zipped', 'zip', 'uploads')
    shutil.rmtree('uploads/')
    os.mkdir('uploads/')

    return render_template('download_success.html')
    

    

    
#Send the organized file zip
@app.route('/download', methods=['GET'])
def download():  

    return send_file('zipped.zip')
    

#Delete the currently uploaded folders
@app.route('/restart', methods=['GET'])
def delete():  
    if os.path.isdir(uploadsPath):
        shutil.rmtree('uploads')
    return redirect('/')


if __name__ == '__main__':
    app.run()




    