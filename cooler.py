from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'GET':
		mintemp = '%2.1f' % gettemp('mintemp')
		maxtemp = '%2.1f' % gettemp('maxtemp')
		temp = '%2.1f' % getcurtemp()
		return render_template("login.html", mintemp = mintemp, maxtemp = maxtemp, temp = temp)
	else:
		mintemp = request.form.get('mintemp')
		if mintemp and mintemp.replace('.','',1).isdigit():
			mintemp = '%2.1f' % float(mintemp)
			settemp('mintemp', mintemp)
		else:
			mintemp = '%2.1f' % gettemp('mintemp')
			
		maxtemp = request.form.get('maxtemp')
		if maxtemp and maxtemp.replace('.','',1).isdigit():
			maxtemp = '%2.1f' % float(maxtemp)
			settemp('maxtemp', maxtemp)
		else:
			maxtemp = '%2.1f' % gettemp('maxtemp')
		
		temp = request.form.get('temp')
		if temp:
			if temp == 'Min+':
				mintemp = '%2.1f' % incmin()
			elif temp == 'Min -':
				mintemp = '%2.1f' % decmin()
			elif temp == 'Max+':
				maxtemp = '%2.1f' % incmax()
			elif temp == 'Max -':
				maxtemp = '%2.1f' % decmax()
			elif temp == 'Turn On':
				os.system("son")
			elif temp == 'Turn Off':
				os.system("soff")
		temp = '%2.1f' % getcurtemp()
		return render_template("login.html", mintemp = mintemp, maxtemp = maxtemp, temp = temp)
	return 'test'

def getcurtemp():
	fp=os.popen('sudo vcgencmd measure_temp | cut -b 6,7,8,9')
	temp=fp.read()
	if temp:
		temp = float(temp)
	else:
		temp = 0.0
	fp.close()
	return temp

def gettemp(name):
	if not os.path.isfile(name+'.txt'):
		fp = open(name+'.txt','w')
		fp.write('30.0\n')
		fp.close()
	fp = open(name+'.txt','r')
	temp = fp.readline()
	temp.replace('.','',1)
	fp.close()
	temp=float(temp)
	return temp

def settemp(name, temp):
	fp = open(name+'.txt','w')
	fp.write(temp)
	fp.close()
	
def incmax():
	fp = open("maxtemp.txt","r")
	temp = float(fp.read()) + 0.2
	fp.close()
	fp = open("maxtemp.txt","w")
	fp.write('%2.1f\n' % (temp))
	fp.close()
	return temp

def decmax():
	fp = open("maxtemp.txt","r")
	temp = float(fp.read()) - 0.2
	fp.close()
	fp = open("maxtemp.txt","w")
	fp.write('%2.1f\n' % (temp))
	fp.close()
	return temp

def incmin():
	fp = open("mintemp.txt","r")
	temp = float(fp.read()) + 0.2
	fp.close()
	fp = open("mintemp.txt","w")
	fp.write('%2.1f\n' % (temp))
	fp.close()
	return temp

def decmin():
	fp = open("mintemp.txt","r")
	temp = float(fp.read()) - 0.2
	fp.close()
	fp = open("mintemp.txt","w")
	fp.write('%2.1f\n' % (temp))
	fp.close()
	return temp
