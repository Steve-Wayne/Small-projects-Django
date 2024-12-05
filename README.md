# To-Do List Application

A simple To-Do List application built using Django. This app allows users to create, update, and delete tasks. Each task can also be marked as completed or not, providing a simple way to track and manage daily tasks.

## Features

- **Task Management**: Create, update, and delete tasks.
- **Task Completion**: Mark tasks as completed or not completed.
- **Simple and Responsive Design**: Uses modern CSS for a clean, user-friendly interface.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default Django database)
- **Version Control**: Git

## Installation

### Prerequisites

- Python 3.x
- Django
- Git (for version control)

### Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/Steve-Wayne/Small-projects-Django.git

Navigate into the project directory:


cd Small-projects-Django
Set up a virtual environment (optional but recommended):


python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the migrations to set up the database:

bash
Copy code
python manage.py migrate
Create a superuser to log in to the Django admin (optional):

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Open the browser and go to http://127.0.0.1:8000 to view the To-Do List application.

Usage
Add a Task: Click the "Add New Task" button and enter the task details.
Edit a Task: Click the "Edit" button next to the task to update its details.
Delete a Task: Click the "Delete" button to remove the task.
Mark as Completed: A task can be marked as completed or not by changing its status.
Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
