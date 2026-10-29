from fastapi import APIRouter, HTTPException
from models.student_model import Student
from controllers import student_controller

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", status_code=201)
def create_student(student: Student):
    return student_controller.create_student(student)

@router.get("/")
def get_all_students():
    return student_controller.get_all_students()

@router.get("/{student_id}")
def get_student(student_id: int):
    student = student_controller.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}")
def update_student(student_id: int, student: Student):
    updated = student_controller.update_student(student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@router.delete("/{student_id}", status_code=204)
def delete_student(student_id: int):
    success = student_controller.delete_student(student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return