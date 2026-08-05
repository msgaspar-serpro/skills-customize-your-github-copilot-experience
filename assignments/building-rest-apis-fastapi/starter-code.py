from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="To-Do API", version="1.0.0")


class Task(BaseModel):
    id: int
    title: str = Field(min_length=1)
    completed: bool = False


tasks: list[Task] = []


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return tasks


# TODO: implementar os endpoints abaixo
# POST /tasks
# GET /tasks/{task_id}
# PUT /tasks/{task_id}
# DELETE /tasks/{task_id}
