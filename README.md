# Flask MVC Task Manager

A simple task management application built with Flask following the MVC (Model-View-Controller) architectural pattern.

![image](https://github.com/user-attachments/assets/df901938-7a67-4c17-9b0c-b4ffdc9f30c9)


## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd flask_mvc_app
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Features

- View all tasks
- Add new tasks
- Delete tasks
- Persistent storage using SQLite
- Clean and modern UI

## Project Structure

```
flask_mvc_app/
├── app.py              # Controller: Handles routes and request logic
├── models.py           # Model: Defines data structure and database models
├── config.py           # Configuration: Database and app settings
├── templates/          # View: HTML templates
│   └── index.html     # Main template for task display
└── requirements.txt    # Project dependencies
```

## MVC Architecture

### Model (models.py)
- Represents the data and business logic
- Defines the database schema using SQLAlchemy ORM
- Handles data validation and relationships
- Contains the `Task` model with properties:
  - id: Unique identifier
  - title: Task description
  - done: Completion status
  - created_at: Timestamp

### View (templates/index.html)
- Handles the presentation logic
- Renders the user interface
- Contains HTML templates and styling
- Displays task list and input form
- No direct database access

### Controller (app.py)
- Handles HTTP requests
- Routes requests to appropriate handlers
- Coordinates between Model and View
- Contains route definitions:
  - GET /: Display all tasks
  - POST /add: Create new task
  - GET /delete/<id>: Remove task


## Database

The application uses SQLite as its database:
- Database file: `tasks.db`
- Automatically created on first run
- Initial sample tasks are added if the database is empty

## Dependencies

- Flask==3.0.2
- Flask-SQLAlchemy==3.1.1

## Development

The application follows these development practices:
- Clean code structure following MVC pattern
- SQLAlchemy for database operations
- Modern UI with responsive design
- Proper error handling
- Configuration separation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License. 
