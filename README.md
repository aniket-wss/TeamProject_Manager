# TeamProject Manager

## Video Demo

[Link to project demo video]

## Description

TeamProject Manager is a web-based application designed to help users manage their projects and tasks. The application allows users to create projects, assign tasks to users, and track the progress of the tasks. It also includes user authentication, so each user has access to their own dashboard and projects.

## How the Program Works

1. **User Authentication:**  
   Users can register an account, log in, and log out. Each user has their own dashboard and can only manage their own projects and tasks.

2. **Project Creation:**  
   After logging in, users can create new projects. Each project contains a title and description, and it's linked to the user who created it.

3. **Task Management:**  
   Once a project is created, users can add tasks to the project. Each task can be assigned to a specific user and contains a title, description, and status (e.g., Not Started, In Progress, Completed).

4. **Dashboard:**  
   The user’s dashboard displays a list of all their projects. For each project, the tasks are listed, allowing users to keep track of progress.

5. **Flask and SQLAlchemy:**  
   The application is built using the Flask web framework and SQLAlchemy for database interactions. User authentication is managed with Flask-Login, and password hashing is done using Werkzeug’s security utilities.

## How the Program Works Internally

- **Flask and Blueprints:**  
  The program uses Flask blueprints to organize routes and handle various aspects of the app like user authentication, project creation, and task management.

- **SQLAlchemy:**  
  SQLAlchemy is used for managing database interactions. It handles the relationships between users, projects, and tasks. For example, each user can create multiple projects, and each project can have multiple tasks.

- **Form Validation:**  
  Flask-WTF is used for form validation. It ensures that user inputs (like project and task titles) meet certain criteria before they are accepted.

## How to Use the Program

1. **Registration:**  
   Users must first register with a username, email, and password. The password is securely hashed before being stored in the database.

2. **Login:**  
   Once registered, users can log in to access their dashboard and start creating projects.

3. **Creating Projects and Tasks:**  
   From the dashboard, users can create projects and assign tasks to different team members. Each task has a status that can be updated as the task progresses.

4. **Managing Tasks:**  
   Users can view all tasks for a given project and track their progress directly from the dashboard.

## Installation

### 1. Clone the Repository

Download the repository using the following command:

```bash
git clone https://github.com/yourusername/teamproject_manager.git
```

### 2. Navigate to the Project Directory

After downloading, open the terminal and navigate to the project directory:

```bash
cd teamproject_manager
```

### 3. Install Required Libraries

Use `pip` to install the required Python libraries. All necessary libraries are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Run the Flask application by executing the following command in the project directory:

```bash
python app.py
```

This will start the development server, and the application will be accessible at `http://127.0.0.1:5000/`.

### Testing the Application

To run tests, use the `pytest` testing framework. The test cases are included in the `test_app.py` file:

```bash
pytest test_app.py
```

## Input and Output

When you run the application:

- **Input:** Users input project details and tasks via forms in the web interface.
  
- **Output:** The user is presented with a dashboard showing their projects and the associated tasks. Task statuses can be updated, and the progress is reflected in real-time.

### Example Images

Here are examples of the program’s input forms and output pages:

#### Dashboard View:

![Dashboard Example](link_to_image)

#### Project Creation Form:

![Project Creation Example](link_to_image)

## Important Notes

- The application includes user authentication, so each user has their own isolated dashboard.
- Project and task data are stored in an SQLite database, which can be migrated to other database systems like PostgreSQL if necessary.
  
## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/)
- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)

---

This `README.md` file provides a clear and detailed explanation of how to set up and run your project. Be sure to update links and any images or videos specific to your project!