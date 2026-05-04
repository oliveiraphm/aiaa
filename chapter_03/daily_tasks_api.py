from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    description: str
    completed: bool

tasks = [
    Task(id=1, description="Buy groceries", completed=False),
    Task(id=2, description="Read a book", completed=True),
    Task(id=3, description="Complete FastAPI project", completed=False),  
]

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks