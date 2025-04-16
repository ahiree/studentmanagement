# Student Management System - Quick Usage Guide

## Setup

1. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. **Configure database:**
   - Create MySQL database: `CREATE DATABASE student;`
   - Set environment variables in `.env` file:
     \`\`\`
     SECRET_KEY=your_secret_key
     DEBUG=True
     DB_NAME=student_db
     DB_USER=your_username
     DB_PASSWORD=your_password
     DB_HOST=localhost
     DB_PORT=3306
     \`\`\`

3. **Initialize application:**
   \`\`\`bash
   python manage.py migrate ,
   python manage.py createsuperuser,
   python manage.py runserver,
   \`\`\`

## Web Interface

1. **Login:** http://localhost:8000/login/

2. **Students List:** http://localhost:8000/students/
   - View all students
   - Click "Add Student" to create new records
   - Use "Edit" and "Delete" buttons for each record

3. **Add Student:** http://localhost:8000/students/create/
   - Fill out the form with student details
   - Click "Save Student"

4. **Edit Student:** http://localhost:8000/students/{id}/update/
   - Update student information
   - Click "Update Student"

## API Usage

1. **Get JWT token:**
   \`\`\`bash
   curl -X POST http://localhost:8000/api/token/ -d "username=your_username&password=your_password"
   \`\`\`

2. **API Endpoints:**
   - List/Create: `GET/POST /api/students/`
   - Retrieve/Update/Delete: `GET/PUT/PATCH/DELETE /api/students/{id}/`

3. **Example API request:**
   \`\`\`bash
   curl -H "Authorization: Bearer your_token" http://localhost:8000/api/students/
   \`\`\`

## Common Issues

- **Authentication errors:** Ensure token is valid and not expired
- **Database errors:** Check MySQL connection settings
- **Permission errors:** Verify user is logged in
