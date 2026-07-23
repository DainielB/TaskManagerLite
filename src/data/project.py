from dataclasses import dataclass

from .entity import Entity


@dataclass
class Project(Entity):

    def __init__(self, name: str, description: str, end_date: str, color: str) -> None:
        super().__init__()

        self._id: str = "" # Create it with uuid
        self.name: str = name
        self.description: str = description
        self.end_date: str = end_date
        # self.start_date: str = start_date
        # self._creation_date: str = creation_date
        # self.state: str = state
        self.color: str = color

    def __str__(self) -> str:
        return f"name: {self.name}, description: {self.description}, end_date: {self.end_date}, color: {self.color}"
