# Gas Utility Service Request Portal

## Screen Shots -
![ScreenShotPro5](https://github.com/user-attachments/assets/f00a14d2-f4b3-4dd1-a0d1-919a3c1a7a52)
![ScreenShotPro2](https://github.com/user-attachments/assets/03e279b2-bbcf-4cb0-9a46-18bc6a223c5e)
![ScreenShotPro3](https://github.com/user-attachments/assets/763faebb-198b-4d4f-8303-21d7e8c81684)
![ScreenShotPro4](https://github.com/user-attachments/assets/b2c3aaba-c5a0-4755-bb1f-b66dfca30837)
![ScreenShotPro](https://github.com/user-attachments/assets/55e84473-018b-4e09-87cd-da1b0ab5a50e)


This Django project provides a web application for managing gas utility service requests from customers.

## Key Features:

## Customer Portal:
1. User registration and login.
2. Create new service requests (e.g., gas leaks, meter reading requests, billing inquiries).
3. Upload images related to the service request.
4. Describe the issue and its severity.
5. Track the status of submitted requests.
6. View historical service request records.

## Admin Panel:
1. Manage customer accounts (using Django Admin).
2. View and manage all service requests.
3. Update request status (e.g., "Pending," "In Progress," "Resolved," "Closed").
4. Assign requests to technicians (if applicable).

# Technologies Used:
1. Django: Python web framework.
2. SQLite: In-memory database for development.
3. Django Forms: This is used to create user-friendly forms for data entry.
4. Django CSRF Protection: To prevent Cross-Site Request Forgery attacks.
5. Django Reloader: For automatic server restarts during development.
6. Tailwind CSS: For styling the user interface.

## Project Structure:
**Project Structure**

*   `gasauthority/` 
    *   `gasauthority/` 
        *   `__init__.py`
        *   `models.py` 
        *   `views.py`
        *   `forms.py`
        *   `urls.py`
        *   `admin.py`
        *   `tests.py` 
        *   `utils.py` 
    *   `customer_service/` 
        *   `__init__.py`
        *   `admin.py`
        *   `models.py` 
        *   `views.py`
        *   `forms.py`
        *   `urls.py`
        *   `apps.py`
        *   `tests.py`
        *   `templates/`
            *  `modify_req`
            *  `register_page`
            *  `service_track_requests`
            *  `submit_req` 
    *   `theme/`
        *   `static/`
            *  `style.css` 
        *   `templates/`
             *   `base`
        *   `statis_src` 
            *   `src/` 
            *   `postcss.config.js`
            *   `tailwind.config.js` 
    *   `templates/` 
        *  `navbar/`
            * `login_page`
            * `navbar`
        * `base`
    *   `db.sqlite3`
    *   `.gitignore`
    *   `manage.py`
    *   `ReadMe.md`
    

## To Run the Project:

1. ```Create a virtual environment: python -m venv venv```
2. ```Activate the environment: source venv/bin/activate (Linux/macOS) or .\venv\Scripts\activate (Windows)```
3. ```Install requirements: pip install -r requirements.txt```
4. ```Run the development server: python manage.py runserver```
