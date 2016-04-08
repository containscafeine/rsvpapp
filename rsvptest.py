import os
import json
import string
import csv
from flask import Flask, render_template, redirect, url_for, request,make_response
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient('192.168.99.100', 27017)
db = client.rsvpdata

@app.route('/')
def rsvpdata():
	_items = db.rsvpdata.find()
	items = [item for item in _items]
	count = len(items)
	print(items)
	return render_template('profile.html',counter=count, items=items)
	

@app.route('/new', methods=['POST'])
def new():
	
	item_doc = {'name': request.form['name'],'email': request.form['email']
}
	db.rsvpdata.insert_one(item_doc)
	return redirect(url_for('rsvpdata'))


@app.route('/csvdata')
def csvdata():

	_items = db.rsvpdata.find()
	k = dumps(_items)
	j = json.dumps(k)
	
    	response = make_response(j)
    	response.headers["Content-Disposition"] = "attachment; filename=rsvp.json"
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
