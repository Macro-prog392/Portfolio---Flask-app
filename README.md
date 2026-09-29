# Flask Portfolio

A personal portfolio website built with Flask, showcasing projects, skills, and contact information.

## Features

- Home / About page
- Projects showcase
- Contact section
- Responsive design

## Tech Stack

- Python 3 / Flask
- Flask-SQLAlchemy (SQLite database)
- Flask-Mail (contact form)
- Jinja2 templates
- HTML/CSS/JS (static assets)
- Gunicorn (production server)

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd <repo-folder>

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root (this is git-ignored):

```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key

# Database
SQLALCHEMY_DATABASE_URI=sqlite:///portfolio.db

# Mail (contact form)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### Running Locally

```bash
flask run
```

Visit `http://127.0.0.1:5000` in your browser.

## Deployment

This project includes a `Procfile` for platforms like Heroku or Render:

```
web: gunicorn app:app
```

Push to your platform of choice and set the required environment variables in its dashboard.

## Project Structure

```
.
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
├── instance/
│   └── portfolio.db
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── templates/
    ├── base.html
    ├── index.html
    └── ...
```

## License

This project is open source and available under the [MIT License](LICENSE).
