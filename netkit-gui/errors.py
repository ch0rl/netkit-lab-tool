from PySide6.QtWidgets import QErrorMessage, QMessageBox


def show_err(title: str, msg: str):
    err = QErrorMessage()
    err.showMessage(msg)
    err.setWindowTitle(title)
    err.exec()


def warn_ask(title: str, msg: str) -> bool:
    win = QMessageBox(QMessageBox.Icon.Warning, title, msg, 
                      QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
    
    return win.exec() == QMessageBox.StandardButton.Ok
