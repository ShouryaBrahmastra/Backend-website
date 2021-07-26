from flask import Flask,redirect,url_for,render_template,request


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo2(db.Model):
    # it is only use for import
    sno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(600), nullable = False)
    message = db.Column(db.String(1600), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    # it is only use for export
    def _repr_(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact' , methods = ["GET","POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

       # data automatically going in the sql server
        todo2 = Todo2(name = name, email = email, message = message)
        db.session.add(todo2)
        db.session.commit()
        return render_template('thank.html')
    return render_template('contactus.html')
  

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies1.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)