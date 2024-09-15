from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=100)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=150)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=150)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    submit = SubmitField('Login')

class CreateProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[InputRequired(), Length(max=200)])
    description = TextAreaField('Description')
    submit = SubmitField('Create Project')

class CreateTaskForm(FlaskForm):
    title = StringField('Task Title', validators=[InputRequired(), Length(max=200)])
    description = TextAreaField('Description')
    status = SelectField('Status', choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    assigned_user_id = SelectField('Assign to', coerce=int)
    submit = SubmitField('Create Task')