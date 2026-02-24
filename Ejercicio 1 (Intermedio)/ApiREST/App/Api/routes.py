from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=List[TaskResponse])
def get_tasks():
    return task_service.get_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str):
    try:
        return task_service.get_task(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    return task_service.create_task(task)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: str, task: TaskUpdate):
    try:
        return task_service.update_task(task_id, task)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: str):
    try:
        task_service.delete_task(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")