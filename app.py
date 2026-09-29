import os
from flask import Flask, request, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__,template_folder='templates',static_folder='static', static_url_path="/")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable= False)
    email = db.Column(db.String(200), nullable= True)
    message = db.Column(db.String(200), nullable= False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable= True)
    
    def __repr__(self):
        return "Task %r" % self.id



@app.route('/')
def index():
 return render_template('Index_Professional_CSS_Rewrite.html')


@app.route('/<name>')
def method_name(name):
    return f"name is {name} "

@app.route('/handle_url_params')
def url_params():
   # return str(request.args)
    name = request.args.get('name')
    password = request.args.get('password')
    return f"{name} , your password is {password}"
    
    
@app.route("/profile")
def getprofile():
    return render_template('macroprofile.html')
    
@app.route("/project")
def project():
    return render_template('project.html')
       
@app.route('/handle_form', methods=['POST','GET'])
def handle_form():
    #db.create_all()
    name = request.form.get('username')
    email = request.form.get('email')
    message = request.form.get('message')
    
    userName = client(id=5,name=name,email=email,message=message)
    try: 
        db.session.add(userName)
        db.session.commit()
        return "connection is successful"
        
    except Exception as e:
        return f"there is some error: {e}, {name} conntacted thriug this email: {email} , messgae follohw: {message}"
    
if __name__ == '__main__':
    #with app.app_context():
       # db.create_all()
        
    app.run(host='0.0.0.0', port='8080',debug=True)