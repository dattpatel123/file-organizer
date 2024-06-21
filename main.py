import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from flask_dropzone import Dropzone
#from groq import Groq
import functions
from zipfile import ZipFile
import shutil


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
dropzone = Dropzone(app)


uploaded = os.path.join(basedir, 'uploads')

# Main Page w/ Dropzone

@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template('index.html')

# Upload File Route
@app.route('/uploadFiles', methods=['POST'])
def uploadFiles():
    
    if 'uploads' not in os.listdir():
        os.mkdir('uploads/')
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(uploaded, f.filename))
        #return redirect(url_for('result'))"""
    return 'uploaded'


#Organize Dropped Files

@app.route('/result', methods=['GET'])
def result():
    
    
    if(len(os.listdir(uploaded)) == 0):
        return render_template('empty.html')
    
    
    functions.organize()
    
    #if(success == 1):
    shutil.make_archive('zipped', 'zip', 'uploads')
    totalInFiles = 0
    for f in os.listdir('uploads'):
        if os.path.isdir('uploads/' + f):
            print(f"{f}: {len(os.listdir('uploads/'+f))}")
            totalInFiles += len(os.listdir('uploads/'+f))
        else:
            print('Extra file: ' + f)

    shutil.rmtree('uploads/')
    os.mkdir('uploads/')

    print(f"Total in Files:{totalInFiles}")
    
    return render_template('download_success.html')
    
    #else:
        #shutil.rmtree('uploads/')
        #return render_template('failed.html')
    

    
#Send the organized file zip

@app.route('/download', methods=['GET'])
def download():  
    return send_file('zipped.zip')


#Delete the currently uploaded folders
@app.route('/delete', methods=['GET'])
def delete():  
   # print(os.listdir('uploads/'))
    shutil.rmtree('uploads')
  #  os.listdir('uploads')
    return 'delete page'

if __name__ == '__main__':
    app.run(debug=True)




    