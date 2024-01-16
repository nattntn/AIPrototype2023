from flask import Flask, request, render_template, make_response 
import json
#import pandas as pd

app = Flask(__name__)

@app.route("/")  #บอกว่าเรียกใช้ web ไหน
def helloworld():
    return "Hello, World!"

@app.route("/name")  #บอกว่าเรียกใช้ web ไหน
def hellonat():
    return "Hello, Nat!"

@app.route("/home2")
def home2():
    # print('we are in home2')
    # # getting input with name = fname in HTML form
    namein = request.form.get['first name']
    print(namein)
    #return render_template("home.html",name = f"{first_name} {last_name}")
    return render_template("home.html",name ='nat')

if __name__ == "__main__":   # run code 
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001