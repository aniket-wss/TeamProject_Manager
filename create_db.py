from app import db, app
from models import User, Project, Task  # Import your models

with app.app_context():
    db.create_all()  # This creates all the tables based on the models

print("Database tables created successfully!")