from flask import Flask,redirect,render_template,request
from flask_mail import Mail,Message

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "gptshourya01@gmail.com"
app.config['MAIL_PASSWORD'] = "gpt2002shourya"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://QVc9ZwoEAb:yxtn9pgVUJ@remotemysql.com/QVc9ZwoEAb'
# DATABSE_URI= 'mysql+mysqlconnector://{QVc9ZwoEAb}:{yxtn9pgVUJ}@{remotemysql.com}/{QVc9ZwoEAb}'.format(user='QVc9ZwoEAb', password='yxtn9pgVUJ', server='remotemysql.com', database='QVc9ZwoEAb')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo1.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_URL'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo1(db.Model):
    # it is only use for import
    sno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(600), nullable = False)
    message = db.Column(db.String(1600), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.now())

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
        todo1 = Todo1(name = name, email = email, message = message)
        db.session.add(todo1)
        db.session.commit()
       # todo1 = Todo1.query.all()
       # print(todo1)

        msg = Message('Hello!!! I will surely reach you as soon as possible',sender = "gptshourya01@gmail.com",recipients=[email])
        msg.body = "Hello buddy glad that you took some precious time out of your busy schedule and filled up this form. I will surely contact you and we will build a great journey ahead of us together."
        #mail.send(msg)
        return render_template('thank.html')
    return render_template('contactus.html')
  

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies1.html')

@app.route('/google')
def google():
    return redirect("https://www.google.com")

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)