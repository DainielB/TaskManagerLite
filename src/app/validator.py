from PySide6.QtGui import QValidator


class Validator(QValidator):

    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input: str, pos: int) -> object:
        print(input, pos)

        if input.strip() == "":
            return self.State.Invalid, input, pos

        # if input is Da

        return self.State.Acceptable, input, pos
