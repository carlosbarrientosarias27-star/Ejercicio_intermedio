from app.core.exceptions import TaskNotFoundException

def get_task(self, task_id: str):
    task = task_repository.get_by_id(task_id)
    if not task:
        raise TaskNotFoundException(task_id)
    return task


def update_task(self, task_id: str, task_data):
    task = self.get_task(task_id)

    if task_data.title is not None:
        task.title = task_data.title

    if task_data.description is not None:
        task.description = task_data.description

    if task_data.completed is not None:
        task.completed = task_data.completed

    return task


def delete_task(self, task_id: str):
    task = self.get_task(task_id)
    task_repository.delete(task)