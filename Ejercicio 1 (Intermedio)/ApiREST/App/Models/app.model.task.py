from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Task:
    id: str
    title: str
    description: str
    completed: bool = False

    @staticmethod
    def create(title: str, description: str):
        return Task(
            id=str(uuid4()),
            title=title,
            description=description,
            completed=False
        )