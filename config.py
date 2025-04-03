import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize SQLAlchemy
db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tasks.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        # Initialize the database with the app
        db.init_app(app)
        
        with app.app_context():
            db.create_all()
            # Import here to avoid circular imports
            from models import Task
            # Add some initial tasks if the database is empty
            if not Task.query.first():
                initial_tasks = [
                    Task(title="Buy groceries"),
                    Task(title="Write blog post"),
                    Task(title="Learn Flask")
                ]
                for task in initial_tasks:
                    db.session.add(task)
                db.session.commit() 