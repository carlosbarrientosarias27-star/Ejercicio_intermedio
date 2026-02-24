from typing import List, Optional
from app.models.task import Task


class TaskRepository:
    def __init__(self):
        self.tasks: List[Task] = []

    def get_all(self) -> List[Task]:
        return self.tasks

    def get_by_id(self, task_id: str) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def create(self, task: Task) -> Task:
        self.tasks.append(task)
        return task

    def update(self, task: Task) -> Task:
        return task

    def delete(self, task: Task) -> None:
        self.tasks.remove(task)


# instancia global simple
task_repository = TaskRepository()