from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import crud
from database import engine, SessionLocal
from schemas import StudentCreate, StudentUpdate, StudentResponse


# Create database tables when the application starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    yield


# Initialize FastAPI application
app = FastAPI(
    title="Student CRUD API",
    description="API for managing student records using FastAPI and SQLite",
    version="1.0.0",
    lifespan=lifespan
)


# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to the Student CRUD API",
        "docs": "/docs"
    }


# CREATE: Add a new student
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    existing_student = (
        db.query(models.Student)
        .filter(models.Student.email == student.email)
        .first()
    )

    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A student with this email already exists"
        )

    return crud.create_student(db, student)


# READ: Get all students, with optional filters
@app.get("/students", response_model=list[StudentResponse])
def read_students(
    skip: int = 0,
    limit: int = 100,
    name: str | None = None,
    course: str | None = None,
    db: Session = Depends(get_db)
):
    if skip < 0:
        raise HTTPException(
            status_code=400,
            detail="skip cannot be negative"
        )

    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="limit must be between 1 and 100"
        )

    query = db.query(models.Student)

    if name:
        query = query.filter(models.Student.name.ilike(f"%{name}%"))

    if course:
        query = query.filter(models.Student.course.ilike(f"%{course}%"))

    return query.offset(skip).limit(limit).all()


# READ: Get one student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


# UPDATE: Update student details
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    update_data = student.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide at least one field to update"
        )

    if "email" in update_data and update_data["email"] is not None:
        existing_student = (
            db.query(models.Student)
            .filter(
                models.Student.email == update_data["email"],
                models.Student.id != student_id
            )
            .first()
        )

        if existing_student:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Another student already uses this email"
            )

    updated_student = crud.update_student(db, student_id, student)

    if updated_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return updated_student


# DELETE: Delete a student
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted_student = crud.delete_student(db, student_id)

    if deleted_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }