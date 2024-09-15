from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, User
from routes import routes  # Import the routes Blueprint

app = Flask(__name__)
app.config.from_pyfile("config.py")

# Initialize db with app
db.init_app(app)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "routes.login"  # Updated to match the Blueprint route

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register the blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)