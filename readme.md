# VideoFlix Backend Setup

Follow the instructions below to set up and run the VideoFlix backend application. This guide covers the Windows environment for general backend tasks and WSL (Linux) for the video conversion service.

---

## 1. Clone the Repository

git clone https://github.com/Wilhelm910/videoflix-backend
cd videoflix-backend

## 2. Create and Activate the Windows Virtual Environment
python -m venv env
Switch into cmd-terminal: "env\Scripts\activate"

## 3. Install Windows Requirements
pip install -r requirements.txt

## 4. Create the .env File for Email Verification Service
In the project root (or inside the /videoflix folder), create a file named .env with the following content (replace with your actual credentials):
EMAIL_HOST_USER=your_host_email_address
EMAIL_HOST_PASSWORD=your_host_email_password

## 5. Set Up the Linux Environment for the Video Conversion Service (WSL)
Open a WSL terminal, navigate to your project folder, and create a Linux virtual environment:
python3 -m venv env-lin
source env-lin/bin/activate
pip install -r requirements-lin.txt

## 6. Initial Backend Setup (Using Windows Environment)
In your activated Windows environment, run the following commands to set up the database and create a superuser:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Then, start the development server:
python manage.py runserver

## 7. Start the RQ Worker (Using WSL Environment)
python manage.py rqworker default

## 8. Adding New Videos via the Admin Dashboard
To add new videos, log in to the Django admin dashboard and navigate to the Videos section. Provide the following required information:

Title
Description
Video File
Category: Enter categories in array format, e.g. ["category1", "category2", ...]
