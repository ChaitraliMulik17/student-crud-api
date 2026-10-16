# Student CRUD API

## Project Overview

The Student CRUD API is a backend application developed using Python, FastAPI, and SQLite. It provides REST API endpoints to create, retrieve, update, and delete student records.

This project was developed as part of an internship assignment for EWB Edu Tech Pvt. Ltd.

## Features

- Create new student records.
- Retrieve all student records.
- Retrieve a student by ID.
- Update existing student information.
- Delete student records.
- Validate input data using Pydantic.
- Validate email addresses.
- Prevent duplicate email addresses.
- Search students by name or course.
- Support pagination using `skip` and `limit`.
- Return appropriate HTTP status codes and error messages.
- Automatically generate interactive API documentation using Swagger UI.

## Technologies Used

- **Python** — Programming language
- **FastAPI** — Web framework for building REST APIs
- **SQLite** — Database for storing student records
- **SQLAlchemy** — Object-relational mapper (ORM)
- **Pydantic** — Data validation and serialization
- **Uvicorn** — ASGI server

## Project Structure

```text
student-crud-app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── requirements.txt
├── README.md
└── students.db
```

The `students.db` file is generated automatically when the application initializes the database.

## Installation and Setup

### 1. Install Python

Install Python 3.10 or later. Python 3.13 was used during development.

### 2. Open the project directory

Open a terminal in the project folder.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m uvicorn main:app --reload
```

The application will start at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI provides interactive documentation through Swagger UI.

Open the following address in your browser after starting the application:

`http://127.0.0.1:8000/docs`

You can use this interface to execute and test the API endpoints.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display the welcome message |
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update a student's information |
| DELETE | `/students/{student_id}` | Delete a student |

### Create a Student

**POST `/students`**

Example request body:

```json
{
  "name": "Aarav Patil",
  "date_of_birth": "2005-08-15",
  "email": "aarav@example.com",
  "phone": "9876543210",
  "course": "Python Backend Development",
  "address": "Pune, Maharashtra",
  "enrollment_date": "2026-10-01"
}
```

### Retrieve All Students

**GET `/students`**

Optional query parameters:

- `skip` — Number of records to skip.
- `limit` — Maximum number of records to return, between 1 and 100.
- `name` — Filter records by student name.
- `course` — Filter records by course.

Example:

`GET /students?skip=0&limit=10`

### Retrieve a Student

**GET `/students/{student_id}`**

Example:

`GET /students/1`

### Update a Student

**PUT `/students/{student_id}`**

Example request body:

```json
{
  "course": "Data Science"
}
```

Only the supplied fields are updated.

### Delete a Student

**DELETE `/students/{student_id}`**

Example:

`DELETE /students/1`

## Database

The application uses SQLite to store student records. SQLAlchemy manages database operations, and the database tables are initialized automatically when the application starts.

Student records include:

- Student ID
- Name
- Date of birth
- Email
- Phone number
- Course
- Address
- Enrollment date

## Error Handling

The API uses appropriate HTTP status codes, including:

- `200 OK` — Successful retrieval, update, or deletion.
- `201 Created` — Student created successfully.
- `400 Bad Request` — Invalid query parameters or an empty update request.
- `404 Not Found` — Student record does not exist.
- `409 Conflict` — Email address is already registered.
- `422 Unprocessable Entity` — Request data failed validation.

## Testing

The API endpoints were tested using the interactive Swagger UI.

The tests included creating a student, retrieving student records, updating a student's course, deleting a student, and verifying that a deleted student could no longer be retrieved.

## Author

Developed as part of an internship assignment for EWB Edu Tech Pvt. Ltd.
```

## Step 2: Save and confirm

After pasting the content:

1. Press **Ctrl + S**.
2. Confirm that the `README.md` tab no longer shows an unsaved-change indicator.
3. Tell me **“README saved.”**

Then we'll check your `requirements.txt` and make sure your project is ready to submit.
