# This code was adapted initially from Cardiff University Gitlab Repository by Natasha Edwards 15-12-2022
# accessed 27-12-2022
# https://git.cardiff.ac.uk/scmne/flask-labs/

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, validators, DateField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp
from portfolio.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired(), Regexp('^[a-z]{6,8}$', message='Your username should be between 6 and 8 characters long, and can only contain lowercase letters.'), EqualTo('confirm_username', message='Usernames do not match. Try again')])
  confirm_username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Username already exist. Please choose a different one.')


class LoginForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

class ProjectForm(FlaskForm):
  title = StringField('Add project title', validators=[DataRequired()])
  content = TextAreaField(u'Add a project description..', [validators.optional()])
  year = TextAreaField('Add year project was completed..', validators=[DataRequired()])
  technologies = TextAreaField('Add technologies in format HTML • CSS • JS..', validators=[DataRequired()])
  image_file = StringField('Add project image..')
  author_id = IntegerField('Select ID..')
  submit = SubmitField("Submit")

class ExpForm(FlaskForm):
  where = TextAreaField(u'Add where..', validators=[DataRequired()])
  exp_type = TextAreaField(u'Work or Education..', validators=[DataRequired()])
  description = TextAreaField(u'Add description..', validators=[DataRequired()])
  dates = TextAreaField(u'Add when you were doing this..', validators=[DataRequired()])
  role = TextAreaField(u'Add role..', validators=[DataRequired()])
  start_date = DateField(u'Enter start date in format of YYYY-MM-DD', validators=[DataRequired()])
  submit = SubmitField("Submit")

class AboutForm(FlaskForm):
  content = TextAreaField(u'Edit About Me description..', validators=[DataRequired()])
  submit = SubmitField("Submit")
