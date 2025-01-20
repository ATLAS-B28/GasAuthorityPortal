##  Gas Utility Service Request Portal

This Django project provides a web application for managing gas utility service requests from customers.

# Key Features:

# Customer Portal:
1. User registration and login.
2. Create new service requests (e.g., gas leaks, meter reading requests, billing inquiries).
3. Upload images related to the service request.
4. Describe the issue and its severity.
5. Track the status of submitted requests.
6. View historical service request records.

# Admin Panel:
1. Manage customer accounts (using Django Admin).
2. View and manage all service requests.
3. Update request status (e.g., "Pending," "In Progress," "Resolved," "Closed").
4. Assign requests to technicians (if applicable).

# Technologies Used:
Django: Python web framework.
SQLite: In-memory database for development.
Django Forms: For creating user-friendly forms for data entry.
Django CSRF Protection: To prevent Cross-Site Request Forgery attacks.
Django Reloader: For automatic server restarts during development.
Tailwind CSS: For styling the user interface.

# Project Structure:


# To Run the Project:

Create a virtual environment: python -m venv venv
Activate the environment: source venv/bin/activate (Linux/macOS) or .\venv\Scripts\activate (Windows)
Install requirements: pip install -r requirements.txt
Run the development server: python manage.py runserver