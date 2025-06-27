# Bot Admin Panel

This project provides a simple Django backend and React frontend for managing a Telegram bot. It includes:

* Django REST API to manage messages
* React-based dashboard served via a template

## Development

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations and start the server:

```bash
cd backend
../manage.py migrate
../manage.py runserver
```

Open `frontend/index.html` in your browser to see the dashboard.
