from flask import Flask,request,render_template

#instance
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])#sort of base directory
def welcome():
    
    name=''
    if request.method=='POST' and 'username' in request.form:
        name=request.form.get('username')
    return render_template("index.html",name=name)

@app.route('/bmi',methods=['GET','POST'])
def grotti():
    bmicalc=''
    if request.method=='POST' and 'weight' in request.form:
        weight1=float(request.form.get('weight'))
        height1=float(request.form.get('height'))
        bmicalc = calc(weight1,height1)
        
    
    
    return render_template("bmi.html",bmicalc=bmicalc)
def calc(weight1,height1):
    return round((weight1/((height1/100)**2)),2)
@app.route('/pegassi')
def peggasi():
    return 'Zenterno'

@app.route('/method',methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return "POST Method"#there is postman google chrome extension that allows to send post request
    else:
        return "GET Method"
    
#if not written nothing will happen
app.run()
