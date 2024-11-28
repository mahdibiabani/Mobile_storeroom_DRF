Mobile Storeroom API
This project provides an API for managing a mobile storeroom. It includes endpoints for authentication, storeroom management, and API documentation.


Installation
Clone the repository

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


run the project on Docker:

docker-compose up


Apply migrations:

docker-compose run web python manage.py migrate


Create a superuser:

docker-compose run web python manage.py createsuperuser


Usage
Once the server is running, you can access the following endpoints:

Admin Panel: http://127.0.0.1:8000/admin/

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

Authentication: http://127.0.0.1:8000/auth/

Storeroom API: http://127.0.0.1:8000/storeroom/


API Documentation
The API documentation is available in two formats:

Swagger UI: Provides an interactive interface to explore and test the API endpoints.
ReDoc: Provides a clean and readable documentation interface.

You can access the documentation at the following URLs:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/
