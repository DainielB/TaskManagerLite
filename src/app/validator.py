from PySide6.QtGui import QValidator


class Validator(QValidator):

    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input_str: str, pos: int) -> object:
        print(f"input: {input_str}, pos: {pos}")

        if input_str.strip() == "":
            return self.State.Invalid, input_str, pos

        if input_str.strip() == "Task Type":
            return self.State.Invalid, input_str, pos

        return self.State.Acceptable, input_str, pos
