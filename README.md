# Task Manager Application
**Overview**
The Task Manager is a web application built using Django and Django REST Framework, designed to help users manage their tasks effectively. 
It provides CRUD (Create, Read, Update, Delete) operations for tasks, allowing users to add, view, update, and delete tasks seamlessly.

*Features*
**Create Task:**
* Add new tasks with title, description, and completion status.
  
**View Task:**
* Retrieve detailed information about a specific task by its ID.
  
**List Tasks:**
* View a list of all tasks with pagination support.
  
**Update Task:**
* Modify details of an existing task.
  
**Delete Task:**
* Remove tasks from the database.

## Technologies Used
* Backend: Django, Django REST Framework
* Database: SQLite (can be configured to other relational databases)
* Frontend: HTML, CSS, JavaScript
* API Documentation: Swagger

## Setup Instructions
**Prerequisites**
* Python 3.x
* Django
* Django REST Framework
* MySQL (or another relational database)

## Installation
***Clone the repository:***
```sh 
git clone https://github.com/alfin-joseph/taskmanagement_bdi.git
cd task-manager
```
***Install Python dependencies:*** 
```sh
pip install -r requirements.txt
```
***Configure Database:***
```sh
python manage.py migrate
```
***Run the development server:***
```sh
python manage.py runserver
```
**Access the application at http://127.0.0.1:8000/.**

### API Documentation
Swagger UI is integrated to provide detailed API documentation and interactive API exploration.
Access the Swagger UI at http://127.0.0.1:8000/swagger/ after starting the server.
### Usage
* Home Page: Displays the task manager interface where users can see the list of tasks and perform CRUD operations.
* Add Task: Form to create a new task.
* Edit Task: Form to update an existing task.
* API Endpoints: Provide RESTful APIs for tasks, ensuring robust and flexible task management.
