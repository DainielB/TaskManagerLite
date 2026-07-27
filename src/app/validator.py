from datetime import date

from PySide6.QtGui import QValidator


class Validator(QValidator):

    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input_str: str, pos: int) -> object:
        print(f"input: {input_str}, pos: {pos}")

        if input_str.strip() == "":
            # Intermediate state, as otherwise the text field does not allow the last character to be deleted.
            return self.State.Intermediate, input_str, pos

        if input_str.strip() == "Task Type":
            return self.State.Invalid, input_str, pos

        return self.State.Acceptable, input_str, pos


class DateValidator(QValidator):

    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input_str: str, pos: int) -> object:
        print(f"date input: {input_str}, pos: {pos}")

        input_date: date = date.fromisoformat(input_str)

        print(f"input_date: {input_date}")

        if input_date > date.today():
            return self.State.Acceptable, input_str, pos

        return self.State.Invalid, input_str, pos
