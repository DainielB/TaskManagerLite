from dataclasses import dataclass

from .entity import Entity


@dataclass
class Task(Entity):

    def __init__(self, name: str, description: str, end_date: str, color: str) -> None:
        super().__init__()

        self._id: str = "" # Create it with uuid
        # self.start_date: str = start_date
        self.end_date: str = end_date
        # self.state: str = ""
        self.description: str = description
        self.name: str = name
        # self.type: str = type
        # self.priority: str = priority
        # self.project: str = project
        # self._creation_date: str = creation_date
        self.color: str = color

    def __str__(self) -> str:
        return f"TASK\r\n name: {self.name}, description: {self.description}, end_date: {self.end_date}, color: {self.color}"
