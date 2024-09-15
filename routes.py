from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Project, Task, db
from forms import LoginForm, RegisterForm, CreateProjectForm, CreateTaskForm

# Create the blueprint
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/dashboard')  # Fixed prefix here
@login_required
def dashboard():
    projects = Project.query.filter_by(creator_id=current_user.id).all()
    return render_template('dashboard.html', projects=projects)

@routes.route('/create_project', methods=['GET', 'POST'])
@login_required
def create_project():
    form = CreateProjectForm()
    if form.validate_on_submit():
        new_project = Project(title=form.title.data, description=form.description.data, creator_id=current_user.id)
        db.session.add(new_project)
        db.session.commit()
        flash('Project Created Successfully!')
        return redirect(url_for('routes.dashboard'))  # Use the blueprint prefix 'routes'
    return render_template('create_project.html', form=form)

@routes.route('/project/<int:project_id>/tasks', methods=['GET', 'POST'])
@login_required
def create_task(project_id):
    project = Project.query.get_or_404(project_id)
    form = CreateTaskForm()
    form.assigned_user_id.choices = [(user.id, user.username) for user in User.query.all()]
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, description=form.description.data, status=form.status.data, project_id=project.id, assigned_user_id=form.assigned_user_id.data)
        db.session.add(new_task)
        db.session.commit()
        flash('Task Created Successfully!')
        return redirect(url_for('routes.dashboard'))  # Use the blueprint prefix 'routes'
    return render_template('create_task.html', form=form, project=project)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('routes.dashboard'))  # Use the blueprint prefix 'routes'
        flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        # Create new user
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # Add and commit to the database
        db.session.add(new_user)
        db.session.commit()

        # Log the user in
        login_user(new_user)
        return redirect(url_for('routes.dashboard'))  # Use the blueprint prefix 'routes'

    return render_template('register.html', form=form)

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))  # Use the blueprint prefix 'routes'