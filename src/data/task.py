from entity import Entity

class Task(Entity):
    type: str  # TODO: This has to be an Enum
    priority: str  # TODO: This has to be an Enum
    project: str  # TODO: This has to be a Project reference, the parent project
