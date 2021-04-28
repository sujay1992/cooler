import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	fp = open("maxtemp.txt","r")
	maxtemp = float(fp.read())
	fp.close()
	fp = open("mintemp.txt","r")
	mintemp = float(fp.read())
	fp.close()
	fp=os.popen('sudo vcgencmd measure_temp | cut -b 6,7,8,9')
	temp=float(fp.read())
	fp.close()
	msg = 'Current Temperature: %2.1f<br/>Minimum Temperature: %2.1f\
	<br/>Maximum Temperature: %2.1f<br/><br/>Use /max+ /max- /min+ \
	/min- to adjust temperature.<br/><br/>Use /max/value /min/value \
	to directly set values.<br/>[Note: Use only float \
	values]' % (temp,mintemp,maxtemp)
	return msg
	
@app.route('/min/<float:temp>')
def setmin(temp):
	os.system('echo %2.1f >mintemp.txt' % temp)
	return 'Minimum temperature updated to %2.1f' % temp

@app.route('/max/<float:temp>')
def setmax(temp):
	os.system('echo %2.1f >maxtemp.txt' % temp)
	return 'Maximum temperature updated to %2.1f' % temp

@app.route('/max+')
def incmax():
	fp = open("maxtemp.txt","r")
	temp = float(fp.read()) + 0.2
	fp.close()
	fp = open("maxtemp.txt","w")
	fp.write('%2.1f\n' % (temp))
	fp.close()
	return 'Maximum temperature increased to %2.1f' % temp

@app.route('/max-')
def decmax():
	fp = open("maxtemp.txt","r")
	temp = float(fp.read()) - 0.2
	fp.close()
	fp = open("maxtemp.txt","w")
	fp.write('%2.1f\n' % (temp))
	fp.close()
	return 'Maximum temperature decreased to %2.1f' % temp

@app.route('/min+')
def incmin():
	fp = open("mintemp.txt","r")
	temp = float(fp.read()) + 0.2
	fp.close()
	fp = open("mintemp.txt","w")
	fp.write('%2.1f\n' % (temp))
	fp.close()
	return 'Minimum temperature increased to %2.1f' % temp

@app.route('/min-')
def decmin():
	fp = open("mintemp.txt","r")
	temp = float(fp.read()) - 0.2
	fp.close()
	fp = open("mintemp.txt","w")
	fp.write('%2.1f\n' % (temp))
	fp.close()
	return 'Minimum temperature decreased to %2.1f' % temp
