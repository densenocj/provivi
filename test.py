from flask import Flask, json, request, render_template_string, render_template, session
from flask_bootstrap import Bootstrap 
import math

#carlos jonathan Castro mendez

api = Flask(__name__)
Bootstrap(api)

@api.route('/')
def index():
    return render_template('index.html')



@api.route('/sum', methods=['GET', 'POST'])
def sum():

    if request.method == 'POST':
        vals = request.form.getlist('suma')
        val1 = float(vals[0])
        val2 = float(vals[1])
        result = val1 + val2
        session['suma'] = result
    else:
        val1 = ''
        val2 = ''
        result = ''
    return render_template('sum.html', val1=val1, val2=val2, result=result)        


@api.route('/prod', methods=['GET', 'POST'])
def prod():

    if request.method == 'POST':
        vals = request.form.getlist('prod')
        val1 = float(vals[0])        
        result = val1 * 2
        
        session['prod'] = result
    else:
        val1 = ''        
        result = ''
    return render_template('product.html', val1=val1, result=result) 

@api.route('/power', methods=['GET', 'POST'])
def power():
    
    if request.method == 'POST':
        vals = request.form.getlist('prod')
        val1 = float(vals[0])        
        result = pow(val1,2)
        session['power'] = result
    else:
        val1 = ''        
        result = ''
    return render_template('power.html', val1=val1, result=result) 
  
@api.route('/all', methods=['GET', 'POST'])
def all():
    
    if request.method == 'GET':
        
        sum=session['suma']
        product = sum * 2
        result = pow(product,2)
        
    else:
        val1 = ''        
        result = ''
    return render_template('all.html', result=result)
  

if __name__ == '__main__':
  api.secret_key = 'super secret key'
  api.config['SESSION_TYPE'] = 'filesystem'      
  #sess.init_app(api)
  api.debug = True
  api.run()