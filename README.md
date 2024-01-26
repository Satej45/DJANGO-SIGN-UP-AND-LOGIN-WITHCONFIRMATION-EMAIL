# Django User Signup, Login, and Email Confirmation

This Django project provides a user authentication system with signup, login, and email confirmation functionalities. It is built using Django, Django Rest Framework, and includes an example frontend for user interactions.

## Features

- User signup with email confirmation.
- User login and authentication.
- Token-based authentication using Django Rest Framework.

## Technologies Used

- Django
- Django Rest Framework
- SQLite (or your preferred database)
- Frontend: HTML, CSS, JavaScript (or use a frontend framework like React, Vue, etc.)

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django (3.x)
- Django Rest Framework

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Satej45/DJANGO-SIGN-UP-AND-LOGIN-WITHCONFIRMATION-EMAIL.git
   cd django-user-authentication
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
  
3. Apply migrations:
    ```bash
   python manage.py migrate

4. Start the development server:
  python manage.py runserver
  Visit http://127.0.0.1:8000/ in your browser.

##Usage
Access the Django Admin interface at http://127.0.0.1:8000/admin/ to manage users and other authentication-related data.
Use the API endpoints for user signup, login, and email confirmation. Refer to the API documentation for details.
API Documentation
API documentation is available at /api/docs/ when the server is running.

##Configuration
Configure your email settings in settings.py for email confirmation functionality.
