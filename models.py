"""
Model Layer (models.py)
----------------------
This file acts as the Model in our MVC pattern. It:
1. Defines the data structure and relationships
2. Contains all business logic and data validation
3. Handles database operations through SQLAlchemy ORM
4. Provides a clean interface for the Controller to interact with data

The Model follows the principle of separation of concerns by:
- Not handling HTTP requests (that's the Controller's job)
- Not handling presentation (that's the View's job)
- Focusing solely on data management and business rules
"""

from datetime import datetime
from config import db

class Task(db.Model):
    """
    Task Model representing a single task in the system.
    This is the core data structure that:
    1. Defines the database schema
    2. Provides data validation
    3. Handles task-specific business logic
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """String representation of the Task model"""
        return f'<Task {self.title}>' 