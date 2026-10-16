from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate, StudentUpdate


# CREATE: Add a new student
def create_student(db: Session, student: StudentCreate):
    student_data = student.model_dump()
    db_student = Student(**student_data)

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


# READ: Get all students
def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()


# READ: Get one student by ID
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


# UPDATE: Modify an existing student
def update_student(
    db: Session,
    student_id: int,
    student_data: StudentUpdate
):
    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    update_data = student_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)

    return db_student


# DELETE: Remove a student
def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return db_student