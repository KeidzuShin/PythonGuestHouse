from flask import Flask, request, render_template, redirect, abort, session
from flask_mail import Mail, Message

from user.UserRouter import userRouter
from book.BookRouter import bookRouter
from room.RoomRouter import roomRouter
from guest.GuestRouter import guestRouter
from service.ServiceRouter import serviceRouter

from user.User import User

from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/guest_house'
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'guesthouse2929@gmail.com'
app.config['MAIL_PASSWORD'] = 'symsmuonfjpftvxs'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

db.init_app(app)

with app.app_context():
  db.create_all()
  
@app.route('/', methods = ['GET', 'POST'])
def index():
  message = None
  if session.get('message'):
    message = session['message']
  session.pop('message', None)
  
  if request.method == 'GET':
    return render_template('index.html', message=message)
  
@app.route('/login', methods = ['GET', 'POST'])
def login():
  if request.method == 'GET':
    message = None
    if session.get('message'):
      message = session['message']
    session.pop('message', None)
  
    return render_template('login.html', message=message)
  
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()
    
    if not user:
      session['message'] = 'Username atau password salah'
      return redirect('/login')
    
    session['username'] = user.username
    session['message'] = 'Login berhasil'
    return redirect('/book')
  
@app.route('/logout', methods = ['GET'])
def logout():
  session['username'] = None
  return redirect('/login')
  
@app.route('/mail', methods = ['POST'])
def sendEmail():
  email = request.form['email']
  msg = Message('Promosi Guest House Terbaru', sender = 'guesthouse2929@gmail.com', recipients = [email])
  html = render_template('promotion.html')
  msg.html = html
  mail.send(msg)
  session['message'] = 'Pesan terkirim, silahkan cek email anda'
  return redirect('/')
  
def isAuthenticated():
  if (session['username'] == None):
    return redirect('/login')
    
@app.route('/dashboard', methods = ['GET'])
def showDashboard():
  if request.method == 'GET':
    return redirect('/book')

app.register_blueprint(userRouter, url_prefix='/user')
app.register_blueprint(roomRouter, url_prefix='/room')  
app.register_blueprint(bookRouter, url_prefix='/book')
app.register_blueprint(guestRouter, url_prefix='/guest')
app.register_blueprint(serviceRouter, url_prefix='/service')

app.before_request_funcs = {
  'user_bp': [isAuthenticated],
  'room_bp': [isAuthenticated],
  'book_bp': [isAuthenticated],
  'guest_bp': [isAuthenticated],
  'service_bp': [isAuthenticated],
}

if __name__ == '__main__':
  app.run(debug=True)