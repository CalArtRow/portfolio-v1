# This code was adapted initially from Cardiff University Gitlab Repository by Natasha Edwards 15-12-2022
# accessed 27-12-2022
# https://git.cardiff.ac.uk/scmne/flask-labs/

from datetime import datetime, date
from portfolio import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Post(db.Model):
  id = db.Column(db.Integer, nullable=False, primary_key=True)
  date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  title = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)
  image_file = db.Column(db.String(40), default='default.jpg')
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  technologies = db.Column(db.Text)
  year = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f"Post('{self.date}', '{self.title}', '{self.content}', '{self.technologies}')"

class Experience(db.Model):
  id = db.Column(db.Integer, nullable=False, primary_key=True)
  place = db.Column(db.Text, nullable=False)
  exp_type = db.Column(db.Text, nullable=False)
  dates = db.Column(db.Text, nullable=False)
  description = db.Column(db.Text)
  role = db.Column(db.Text, nullable=False)
  start_date = db.Column(db.Date, nullable=False)

  def __repr__(self):
    return f"Post('{self.place}', '{self.exp_type}', '{self.dates}, '{self.description}', '{self.role}', '{self.start_date}')"

class About(db.Model):
  id = db.Column(db.Integer, nullable=False, primary_key=True)
  profile_image = db.Column(db.String(40), nullable=False)
  content = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f"Post('{self.content}')"


class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), unique=True, nullable=False)
  hashed_password=db.Column(db.String(128))
  post = db.relationship('Post', backref='user', lazy=True)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

  #adpated from Grinberg(2014, 2018)
  @property
  def password(self):
    raise AttributeError('Password is not readable.')

  @password.setter
  def password(self,password):
    self.hashed_password=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.hashed_password,password)


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


