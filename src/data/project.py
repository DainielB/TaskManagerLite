from dataclasses import dataclass

from .entity import Entity


@dataclass
class Project(Entity):
    # tasks: list

    def __init__(self, name: str, description: str, end_date: str, color: str) -> None:
        super().__init__()
        self.name: str = name
        self.description: str = description
        # self.end_date: str = end_date
        self.color: str = color

    def __str__(self) -> str:
        return f"name: {self.name}, description: {self.description}, end_date: {self.end_date}, color: {self.color}"
