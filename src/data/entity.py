from datetime import date


class Entity:
    id: str = ""
    name: str = ""
    description: str = ""
    start_date: date = None
    end_date: date = None
    _creation_date: date = None
    status: str = ""  # TODO: This has to be an Enum
