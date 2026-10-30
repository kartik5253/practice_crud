from fastapi import FastAPI
from routers.student_routes import router as student_router

app = FastAPI(title="Student manaignggit init")

app.include_router(student_router)