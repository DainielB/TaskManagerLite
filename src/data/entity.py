from datetime import date


class Entity:
    id: str = ""
    name: str = ""
    description: str = ""
    start_date: date = None
    end_date: date = None
    date_of_creation: date = None
    state: str = ""  # TODO: This has to be an Enum
