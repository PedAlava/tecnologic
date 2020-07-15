from flask import Flask, request, jsonify, render_template
#from wtforms import Form
#from wtforms import StringField
import os
import requests
import json
import pusher

import forms
import Skynet

app = Flask(__name__)

@app.route('/')
def index():
	title = "Tecnologic Store Ups"
	return render_template('tecno.html',title=title)

@app.route('/mains')
def mains():
	return render_template('inicio.html')
@app.route('/main')	
def main():
	return render_template('dashboard.html')

@app.route('/cell')	
def cell():
	return render_template('celulares.html')

@app.route('/cells')	
def cells():
	title = "Celulares Inteligentes"
	return render_template('prod.html',title=title)

@app.route('/lap')	
def lap():
	return render_template('prod.html')

@app.route('/laps')	
def laps():
	title = "Laptops"
	return render_template('prod.html',title=title)

@app.route('/novs')	
def novs():
	title = "Productos Novedosos"
	return render_template('prod.html',title=title)

@app.route('/nov')	
def nov():
	return render_template('novedades.html')

@app.route('/buy')	
def buy():
	return render_template('venta.html')

@app.route('/check')	
def check():
	title = "Checkout"
	return render_template('checkout.html',title=title)

@app.route('/store')	
def store():
	title = "Store"
	return render_template('store.html',title=title)

@app.route('/asistence')
def asistence():
	comment_form = forms.CommentForm(request.form)
	#title = "Chat Prueba"
	return render_template('asist.html',form =comment_form)

@app.route('/asist')
def asist():
	comment_form = forms.CommentForm(request.form)
	title = "Asistente"
	return render_template('asistente.html',title=title,form =comment_form)


@app.route('/send_message',methods=['GET','POST'])
def send_message():
	
	id = request.form['id']
	message = request.form['message']
	response = { "id":id,"name": "Cliente","id_chat":id,"message": message }
	#requests.post("https://us-central1-tecnologic-store-ups-4aade.cloudfunctions.net/coversations", response )
	response_message = Skynet.respon(message)
	cd = int(id)
	cd += 1
	response_text = { "id":id,"name": "Skynet","id_chat":id,"message": response_message }
	#requests.post("https://us-central1-tecnologic-store-ups-4aade.cloudfunctions.net/coversations", response_text )
	
	print(response)
	print(response_text)
	return jsonify(**response_text)


# run Flask app
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)