import requests
import urllib
import json
import os
from flask import Flask,render_template,send_file,request,url_for,session,redirect

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/gdrive',methods = ['POST', 'GET'])
def gdrive():
	if (request.method == 'POST'):
		url=request.form["mssg"]
		idurl=url[32:-17]
		newurl=url[:25]+"uc?id="+idurl+"&export=download"
		return render_template('index.html',y=newurl)
	return render_template('index.html')

@app.errorhandler(404)
def error(e):
	return render_template('error.html')
@app.errorhandler(500)
def server():
	return render_template('server-error.html')
if __name__=="__main__":
    app.run()
