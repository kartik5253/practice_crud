from fastapi import FastAPI
from routers.student_routes import router as student_router

app = FastAPI(title="Student CRUD Practice API")

app.include_router(student_router)