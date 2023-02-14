from flask import Flask, jsonify, render_template, request
import os
import datetime
from firebase_admin import credentials, initialize_app, firestore
from key import creds
import firebase_admin

app = Flask(__name__)






firebase_db = firestore.client()

@app.route("/add-data", methods=["POST"])
def add_data():
    try:
       
       
       
       
       
       
       
       
        return jsonify({
            "status": "success"
        }), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@app.route("/")
def index():
   
   
   
   
   
   
   
   
   
   
   
   
   

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='   ', port=5000)