# TeamProject Manager

## Project Overview

**TeamProject Manager** is a web-based application designed to streamline the management of projects and tasks within a team setting. It allows users to create projects, assign tasks to team members, and monitor progress. The goal is to offer a simple, intuitive interface for project management, providing both team members and managers with a platform to collaborate efficiently.

This project leverages **Flask**, **Flask-SQLAlchemy**, and **Flask-Login** to handle user authentication and session management, while **SQLite** is used as the database to store user data, projects, and tasks. The application focuses on task delegation, project tracking, and team collaboration, making it easy for team members to know what tasks are assigned to them and the overall project status.

## File Structure and Functionality

### 1. **app.py**
This is the entry point of the application. It initializes the Flask app and sets up the necessary configurations for database connections and user sessions. The app uses `Flask-SQLAlchemy` to manage the database and `Flask-Login` to handle user authentication. The `@login_manager.user_loader` is used to load users during their sessions.

Key functions:
- **`db.create_all()`**: Ensures all the database tables are created before the app runs.
- **`load_user(user_id)`**: Retrieves a user by their ID during login sessions.
- **App context setup**: Ensures that the app is correctly instantiated and running in debug mode for development.

### 2. **routes.py**
This file manages all the core routes of the application. It acts as the bridge between the user interface (HTML templates) and the business logic. The routes are grouped using Flask's Blueprint feature to keep the code modular.

Key routes:
- **`/` (index)**: Displays the homepage of the application.
- **`/dashboard`**: Shows the dashboard with an overview of the projects and tasks assigned to the logged-in user.
- **`/create_project`**: Allows users to create new projects.
- **`/project/<int:project_id>/tasks`**: Displays and allows the creation of tasks for a specific project.
- **`/login` and `/register`**: Handle user authentication and registration.
- **`/logout`**: Logs the user out and redirects to the homepage.

### 3. **models.py**
This file defines the database models using SQLAlchemy. It includes three key models: **User**, **Project**, and **Task**. These models outline the structure of the database and its relationships, allowing the app to interact with the stored data.

- **User model**: Stores user information such as `username`, `email`, and `password`. It also has relationships with the Project and Task models to link users to their respective projects and tasks.
- **Project model**: Represents a project created by a user. It contains fields like `title`, `description`, and `creator_id`. The project is linked to the tasks via a foreign key relationship.
- **Task model**: Contains information about individual tasks, including the `title`, `description`, `status`, and the assigned user. Each task is associated with a project and a user.

### 4. **forms.py**
This file contains the forms used in the application, defined using Flask-WTF. The forms are used to capture user input for registering, logging in, creating projects, and creating tasks.

Key forms:
- **RegisterForm**: Captures the user’s `username`, `email`, and password during registration.
- **LoginForm**: Captures the `email` and password for user login.
- **CreateProjectForm**: Allows the user to provide a title and description when creating a new project.
- **CreateTaskForm**: Captures the task’s `title`, `description`, status, and assigns the task to a user.

### 5. **templates** (HTML files)
The HTML templates provide the front-end views for the application. Flask's Jinja2 template engine is used for dynamic rendering. The templates extend from a base layout and are structured to keep the design consistent.

- **base.html**: The base layout, containing the header and navigation menu.
- **index.html**: The homepage of the app.
- **dashboard.html**: Displays an overview of all projects and tasks for the logged-in user.
- **create_project.html**: Provides the form for creating new projects.
- **create_task.html**: Contains the form for creating and assigning tasks to team members.
- **login.html** and **register.html**: Handle user login and registration.

### 6. **static/styles.css**
This file contains the custom CSS used to style the application's interface. It defines the layout, colors, and overall look of the forms, buttons, and navigation.

### 7. **config.py**
This file holds the configuration settings for the app, such as the secret key for sessions and the database URI. In this case, the database used is SQLite.

### 8. **requirements.txt**
Lists all the dependencies required to run the application. Some key dependencies include:
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF

Users can install these dependencies using the command:
```
pip install -r requirements.txt
```

## Design Choices

### 1. **Database Choice**
I chose **SQLite** for simplicity and ease of setup. SQLite works well for small to medium-sized applications like this and requires no separate server configuration, making it ideal for rapid development.

### 2. **Modular Blueprint Structure**
The use of Flask Blueprints allows the application to remain modular. This is particularly useful when scaling the app, as different components (like user management or project management) can be separated into their own modules.

### 3. **User Authentication**
Flask-Login handles user authentication seamlessly, allowing the app to manage sessions and restrict access to certain routes. I opted for hashed passwords using the `pbkdf2:sha256` algorithm to ensure secure storage of user credentials.

### 4. **Task Delegation**
The ability to assign tasks to specific team members is a key feature. It enhances the collaborative aspect of the app, ensuring that team members have clarity on their responsibilities within a project.

## Challenges and Future Improvements

One of the key challenges was managing the relationships between users, projects, and tasks in a way that was efficient yet flexible. Handling user roles (like managers vs. team members) could be a feature for future improvements. Adding more complex features like real-time updates or notifications when tasks are updated would also enhance user experience.

In the future, I would also consider expanding this app to include features like time tracking, progress reports, and integrations with third-party tools like Slack or Trello.

## Installation and Usage

1. Clone the repository:
```
git clone https://github.com/aniket_wss/TeamProject_Manager.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Run the Flask app:
```
python app.py
```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

5. To run tests, use the following command:
```
pytest test_app.py
```

