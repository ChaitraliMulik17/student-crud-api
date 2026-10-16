from datetime import date
from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    date_of_birth: date
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    course: str | None = None
    address: str | None = None
    enrollment_date: date | None = None


class StudentUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    date_of_birth: date | None = None
    email: EmailStr | None = None
    phone: str | None = Field(None, min_length=10, max_length=15)
    course: str | None = None
    address: str | None = None
    enrollment_date: date | None = None


class StudentResponse(BaseModel):
    id: int
    name: str
    date_of_birth: date
    email: EmailStr
    phone: str
    course: str | None = None
    address: str | None = None
    enrollment_date: date | None = None

    class Config:
        from_attributes = True