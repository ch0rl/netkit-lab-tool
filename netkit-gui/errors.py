from PySide6.QtWidgets import QErrorMessage


def show_err(title: str, msg: str):
    err = QErrorMessage()
    err.showMessage(msg)
    err.setWindowTitle(title)
    err.exec()
