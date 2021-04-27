import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Use /max/<temp> or /min/<temp> to update temperature values.<br/>[Note: Use only float values]"
	
@app.route('/min/<float:temp>')
def setmin(temp):
	os.system('echo %2.1f >mintemp.txt' % temp)
	return 'Minimum temperature updated to %2.1f' % temp

@app.route('/max/<float:temp>')
def setmax(temp):
	os.system('echo %2.1f >maxtemp.txt' % temp)
	return 'Maximum temperature updated to %2.1f' % temp
