from uuid import UUID, uuid4

from PySide6.QtCore import QDate, QObject

from constants import DATE_FORMAT


class Entity(QObject):

    def __init__(self, name: str, end_date: QDate, description: str = "", id: str = None) -> None:
        super().__init__()

        self._id: str = str(uuid4()) if not id else id
        self._name: str = name
        self._start_date: QDate = None
        self._end_date: QDate = end_date
        self._description: str = description
        self._creation_date: QDate = QDate.currentDate()

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def start_date(self) -> str:
        return self._start_date.toString(DATE_FORMAT) if self._start_date else ""

    @start_date.setter
    def start_date(self, start_date: QDate) -> None:
        self._start_date = start_date

    @property
    def end_date(self) -> str:
        return self._end_date.toString(DATE_FORMAT)

    @end_date.setter
    def end_date(self, end_date: QDate) -> None:
        self._end_date = end_date

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def creation_date(self) -> str:
        return self._creation_date.toString(DATE_FORMAT)
