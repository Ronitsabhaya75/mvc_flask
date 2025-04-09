"""
Controller Layer (app.py)
------------------------
This file acts as the Controller in our MVC pattern. It:
1. Handles all HTTP requests and routes
2. Coordinates between Model (models.py) and View (templates)
3. Processes user input and updates the Model accordingly
4. Renders the appropriate View with data from the Model

The Controller follows the principle of separation of concerns by:
- Not containing any business logic (that's in the Model)
- Not containing any presentation logic (that's in the View)
- Only handling request/response flow and data coordination

Added the new feature:
- Toggle task completion status
  - This feature allows users to mark tasks as completed or not completed.
  - It updates the task's status in the database and refreshes the task list.
  - This is done through a new route '/toggle/<task_id>' that changes the 'done' attribute of the Task model.
"""

from flask import Flask, render_template, request, redirect, url_for
from models import Task
from config import Config, db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the application
Config.init_app(app)

@app.route('/')
def index():
    """
    Controller action that:
    1. Gets all tasks from the Model
    2. Passes them to the View for rendering
    """
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """
    Controller action that:
    1. Receives form data from the View
    2. Creates a new task in the Model
    3. Redirects back to the index View
    """
    title = request.form['title']
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """
    Controller action that:
    1. Receives task ID from the View
    2. Deletes the task from the Model
    3. Redirects back to the index View
    """
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Toggle task completion status"""
    task = Task.query.get_or_404(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 