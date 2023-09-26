# This code was adapted initially from Cardiff University Gitlab Repository by Natasha Edwards 15-12-2022
# accessed 27-12-2022
# https://git.cardiff.ac.uk/scmne/flask-labs/

from flask import render_template, url_for, request, redirect, flash
from portfolio import app, db
from portfolio.models import User, Post, Experience, About
from portfolio.forms import RegistrationForm, LoginForm, ProjectForm, ExpForm, AboutForm
import os
import smtplib
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import desc

# Homepage route - displays all the posts and the about me section
@app.route("/")
@app.route("/home")
def home():
  posts = Post.query.all()
  about = About.query.get(1)
  experience = Experience.query.order_by(desc(Experience.start_date))
  return render_template('home.html',posts=posts, about=about, experience=experience)


# Admin login route
@app.route("/admin", methods=['GET','POST'])
def admin():
  form = LoginForm()
  about = About.query.get(1)
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('You\'ve successfully logged in,'+' '+ current_user.username +'!')
      return redirect(url_for('admin'))
    flash('Invalid username or password.')

  return render_template('admin.html', title='Login',form=form, about=about)

#About me route
@app.route("/about")
def about():
  about = About.query.get(1)
  return render_template('about.html', title='About', about=about)

# Edit about me route, only accessible when logged in
@app.route("/about/edit", methods=['GET','POST'])
@login_required
def edit_about():
    about = About.query.get(1)
    form = AboutForm()
    if form.validate_on_submit():
      about.content = form.content.data
      # Update database
      db.session.add(about)
      db.session.commit()
      flash("About me has been updated!")
      return redirect(url_for('about'))

    form.content.data = about.content
    return render_template('edit_about.html', form=form, about=about)

# Individual project/post route
@app.route("/post/<int:post_id>")
def post(post_id):
  post = Post.query.get_or_404(post_id)
  return render_template('post.html', title=post.title, post=post)  

# Projects route, retrieves all projects
@app.route("/projects", methods=['POST', 'GET'])
def projects():
    projects = Post.query.order_by(Post.date)
    return render_template('projects.html', title='Projects', projects=projects) 


@app.route('/projects/add', methods=['GET', 'POST'])
@login_required
def add_project():
  projects = Post.query.order_by(Post.date)
  form = ProjectForm()

  if form.validate_on_submit():
    project = Post(title=form.title.data, content=form.title.data, year=form.year.data, technologies=form.technologies.data, image_file=form.image_file.data)
    db.session.add(project)
    db.session.commit()
    flash("Project Added Successfully!")

  title = form.title.data
  content = form.content.data
  year = form.year.data
  technologies = form.technologies.data
  image_file = form.image_file.data
  form.title.data = ''
  form.content.data = ''
  form.year.data = ''
  form.technologies.data = ''
  form.image_file.data = ''

  our_projects = Post.query.order_by(Post.year)

  return render_template("add_project.html", projects=projects, form=form, title=title, content=content, our_projects=our_projects, year=year, technologies=technologies, image_file=image_file)


@app.route('/delete/<int:id>')
@login_required
def delete(id):
  project_to_delete = Post.query.get_or_404(id)
  projects = Post.query.order_by(Post.date)
  form = ProjectForm()
  title = form.title.data
  content = form.content.data
  our_projects = Post.query.order_by(Post.date)

  try:
    db.session.delete(project_to_delete)
    db.session.commit()
    flash("Project Info Deleted Successfully!!")

    our_projects = Post.query.order_by(Post.date)

    return render_template("add_project.html", projects=projects, form=form, title=title, content=content, our_projects=our_projects)
  
  except:
    flash("Sorry there was a problem deleting the project, try again...")
    return render_template("add_project.html", projects=projects, form=form, title=title, content=content, our_projects=our_projects)

@app.route("/work_experience")
def work():
  experience = Experience.query.order_by(desc(Experience.start_date))
  return render_template('work_experience.html', experience=experience) 

@app.route('/work_experience/add', methods=['GET', 'POST'])
@login_required
def add_work():
  experiences = Experience.query.order_by(Experience.start_date)
  form = ExpForm()

  if form.validate_on_submit():
    experience = Experience(place=form.where.data, exp_type=form.exp_type.data, dates=form.dates.data, description=form.description.data, role=form.role.data, start_date=form.start_date.data)
    db.session.add(experience)
    db.session.commit()
    flash("Experience Info Added Successfully!")

  where = form.where.data
  exp_type = form.exp_type.data
  dates = form.dates.data
  description = form.description.data
  role = form.role.data
  start_date = form.start_date.data
  form.where.data = ''
  form.exp_type.data = ''
  form.dates.data = ''
  form.description.data = ''
  form.role.data = ''
  form.start_date.data = ''
  
  our_experiences = Experience.query.order_by(Experience.start_date)

  return render_template("add_experience.html", form=form, experiences=experiences, where=where, exp_type=exp_type, dates=dates, description=description, role=role, start_date=start_date, our_experiences=our_experiences)

@app.route('/work_experience/<int:id>')
@login_required
def delete_work(id):
  exp_to_delete = Experience.query.get_or_404(id)
  experiences = Experience.query.order_by(Experience.start_date)
  form = ExpForm()
  where = form.where.data
  exp_type = form.exp_type.data
  dates = form.dates.data
  description = form.description.data
  role = form.role.data
  start_date = form.start_date.data
  our_experiences = Experience.query.order_by(Experience.start_date)

  try:
    db.session.delete(exp_to_delete)
    db.session.commit()
    flash("Experience Info Deleted Successfully!!")

    our_projects = Post.query.order_by(Post.date)

    return render_template("add_experience.html", exp_to_delete=exp_to_delete, experiences=experiences , form=form, where=where, exp_type=exp_type, dates=dates, description=description, role=role, start_date=start_date, our_experiences=our_experiences)
  
  except:
    flash("Sorry there was a problem deleting the experience info, try again...")
    return render_template("add_experience.html", exp_to_delete=exp_to_delete, experiences=experiences , form=form, where=where, exp_type=exp_type, dates=dates, description=description, role=role, start_date=start_date, our_experiences=our_experiences)


@app.route("/contact")
def contact():
  return render_template('contact.html', title='contact')   

@app.route("/cv")
def cv():
  return render_template('cv.html', title='CV')  

@app.route('/contact/sent', methods=['POST'])
def send_email():
  
  email = request.form.get('email')
  message = request.form.get('message') + email
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login("calebrowlands94@gmail.com", os.environ['EMAIL_PASSWORD'])
  server.sendmail(email, 'calebrowlands94@gmail.com', message)
  
  if not email or not message:
    error_statement = "All form fields are required.."
    return render_template('form_error.html', error_statement=error_statement, email=email, message=message)

  flash("Email successully sent!")
  return render_template('/email_sent.html', email=email, message=message)

@app.route("/logout")
def logout():
  logout_user()
  flash('Logout successful. Bye!')
  return redirect(url_for('home'))


@app.errorhandler(404)
def e_404_not_found(e):
    return render_template("404.html")

@app.errorhandler(401)
def e_401_not_found(e):
    return render_template("401.html")
