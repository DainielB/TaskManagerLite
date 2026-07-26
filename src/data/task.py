from dataclasses import dataclass
from datetime import date


from .entity import Entity


@dataclass
class Task(Entity):

    def __init__(self, name: str, end_date: date, type: str) -> None:
        super().__init__()

        self._id: str = "" # Create it with uuid
        # self.start_date: date = start_date
        self.end_date: date = end_date
        self.status: str = ""
        self.description: str = ""
        self.name: str = name
        self.type: str = type
        self.priority: str = ""
        # self.project: str = project
        # self._creation_date: date = creation_date
        # self.color: str = color

    def __str__(self) -> str:
        return f"TASK\r\n name: {self.name}, description: {self.description}, end_date: {self.end_date}, color: {self.color}"
