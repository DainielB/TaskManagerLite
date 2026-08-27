from abc import ABC, abstractmethod
from uuid import UUID, uuid4

from PySide6.QtCore import QDate, QObject

from constants import TaskStatus


class Entity(QObject):

    def __init__(self, name: str, end_date: QDate, status: TaskStatus = TaskStatus.TO_DO, description: str = "") -> None:
        super().__init__()
        self._id: UUID = uuid4()
        self._name: str = name
        self._start_date: QDate = None # Set when TaskStatus changes to IN_PROGRESS
        self._end_date: QDate = end_date
        self._status: TaskStatus = status
        self._description: str = description
        self._creation_date: QDate = QDate.currentDate()

    '''
    @abstractmethod
    def __str__(self) -> str:
        ...
    '''

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def start_date(self) -> QDate:
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: QDate) -> None:
        self._start_date = start_date

    @property
    def end_date(self) -> QDate:
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: QDate) -> None:
        self._end_date = end_date

    @property
    def status(self) -> TaskStatus:
        return self._status

    @status.setter
    def status(self, status: TaskStatus) -> None:
        self._status = status

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def creation_date(self) -> QDate:
        return self._creation_date

    """
    @creation_date.setter
    def creation_date(self, creation_date: QDate) -> None:
        self._creation_date = creation_date
    """
