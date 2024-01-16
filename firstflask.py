from flask import Flask,  flash, redirect, request, render_template, make_response, url_for
import json
import sys 
#import pandas as pd

app = Flask(__name__)

@app.route("/")  #บอกว่าเรียกใช้ web ไหน
def helloworld():
    return "Hello, World!"

@app.route("/name")  #บอกว่าเรียกใช้ web ไหน
def hellonat():
    return "Hello, Nat!"

@app.route("/home", methods=['POST','GET']) # methods=['POST'] ต้องเปิดเพื่อให้รับข้อความ
def homefn():
    if request.method == "GET":
       print('we are in home(GET)', file=sys.stdout)

       namein = request.args.get('fname')
       print(namein, file=sys.stdout)
       return render_template("home.html",name=namein)

    elif request.method == "POST":
        print('we are in home(POST)', file=sys.stdout)
        namein = request.form.get('fname') #เก็บ input
        lastnamein = request.form.get('lname')
        print(namein, file=sys.stdout)
        print(lastnamein, file=sys.stdout)
        #return render_template("home.html",name = f"{first_name} {last_name}")
        return render_template("home.html",name=namein)

@app.route('/upload', methods=['GET', 'POST'])  # เริ่มเเรก Get ไป return
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('filename')
        return render_template("home.html",name= 'upload completed')

    return '''  
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":   # run code 
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001