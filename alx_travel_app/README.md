ALX Travel App – Backend API (Django + DRF + MySQL)

A real-world backend system for a travel listing platform, built using Django, Django REST Framework, and MySQL, following professional software engineering standards.

This project is part of the ALX Backend Specialization and represents Milestone 1 & Milestone 2 combined:
✔ Project Setup & Configuration
✔ Database Integration (MySQL)
✔ Listings, Bookings, and Reviews Models
✔ Serializers
✔ Seeder Script
✔ API Documentation (Swagger & ReDoc)

🚀 Project Objectives

This project teaches you how to:

Bootstrap a production-ready Django project

Structure backend components professionally

Configure MySQL database connections

Use environment variables for secure configuration

Implement API documentation with Swagger

Create models, serializers, and seeders

Handle migrations and database operations

Debug real-world backend errors

Work with Git and GitHub collaboratively

📦 Technologies Used
Tool	Purpose
Django	Main backend framework
Django REST Framework	API development
MySQL	Main database
django-environ	Load environment variables
drf-yasg	Swagger & ReDoc documentation
Faker	Seeder script for sample data
Git	Version control
Postman	API testing
📁 Project Structure
alx_travel_app/
│
├── alx_travel_app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── listings/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── management/
│       └── commands/
│           └── seed.py
│
├── requirements.txt
├── README.md
└── manage.py

🛠 Setup Guide
1️⃣ Clone the Repository
git clone https://github.com/Freddanjuma/alx_travel_app_0x00.git
cd alx_travel_app_0x00

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


If Faker is not included:

pip install Faker

4️⃣ Create .env File

Create:

alx_travel_app/.env


Add MySQL configuration:

DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=travel_app
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306

5️⃣ Connect Django to MySQL

Make sure your MySQL server is running:

mysql -u root -p


Create database:

CREATE DATABASE travel_app;

6️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

7️⃣ Create Superuser
python manage.py createsuperuser

8️⃣ Run Development Server
python manage.py runserver

🧪 API Documentation

📘 Swagger UI
👉 http://localhost:8000/swagger/

📕 ReDoc
👉 http://localhost:8000/redoc/

🔐 Django Admin
👉 http://localhost:8000/admin/

🌱 Running the Seeder

The seeder inserts sample listings into the database.

python manage.py seed

✔ Milestone 2 Components
Models Implemented

Listing

Booking

Review

Serializers Implemented

ListingSerializer

BookingSerializer

Seeder Implemented

/listings/management/commands/seed.py

🛑 Common Errors & Debugging Guide
❗Error 1:
ModuleNotFoundError: No module named 'messaging_app'

Cause:
You referenced a non-existent app in your ForeignKey.

Fix:
Replace:

ForeignKey('messaging_app.User')


With:

ForeignKey(settings.AUTH_USER_MODEL)

❗Error 2:
django.core.exceptions.ImproperlyConfigured: DEFAULT_AUTO_FIELD refers to ... listings.User

Cause:
You accidentally defined a model named User inside listings.

Fix:
Remove any class named User inside models.py.

❗Error 3:
pip Fatal error in launcher: Unable to create process

Cause:
Wrong Python path stored in venv during duplication.

Fix:
Delete and recreate venv:

rm -rf venv
python -m venv venv
pip install -r requirements.txt

❗Error 4:
MySQL connection error: "2003: Can't connect to MySQL server"

Fix:

Start MySQL service

Ensure correct password

Ensure port = 3306

Ensure .env is correctly loaded

❗Error 5:
Migration error: missing tables

Fix:

python manage.py makemigrations
python manage.py migrate --run-syncdb

📬 Postman Collection (Optional)

I can generate one for you — just tell me.

🖼 Screenshots Section (Optional)

Add your screenshots here:

/screenshots/
    swagger.png
    admin.png
    db_schema.png

👥 Contributing Guidelines

Fork the repository

Create a feature branch

Commit with clear messages

Submit PR

📝 License

This project is licensed for educational use under the ALX Scholarship program.


