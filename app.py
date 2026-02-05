from flask import Flask,render_template,request
import pandas as pd
app=Flask(__name__)

def assess(f):
    df=pd.read_csv(f)
    r,e,c,l,rec=df.iloc[0]
    risk=0
    if e>0.8*r: risk+=30
    if c<0.1*r: risk+=25
    if l>0.5*r: risk+=25
    if rec>0.3*r: risk+=20
    risk=min(risk,100)
    level='Low Risk' if risk<=30 else 'Medium Risk' if risk<=60 else 'High Risk'
    return risk,level

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        f=request.files['file']
        risk,level=assess(f)
        return render_template('index.html',risk=risk,level=level)
    return render_template('index.html')

app.run()
