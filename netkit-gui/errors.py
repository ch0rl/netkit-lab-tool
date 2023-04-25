from PySide6.QtWidgets import QErrorMessage, QMessageBox


def show_err(title: str, msg: str):
    """Creates an error message popup
    
    Args:
        title: the window title of the popup
        msg: the error message to display
    """
    
    err = QErrorMessage()
    err.showMessage(msg)
    err.setWindowTitle(title)
    err.exec()


def warn_ask(title: str, msg: str) -> bool:
    """Creates a warning dialog, returning the result
    
    Args:
        title: the window title of the dialog
        msg: the warning message
    Returns:
        bool: True if the user pressed 'Ok', False otherwise
    """
    
    win = QMessageBox(QMessageBox.Icon.Warning, title, msg, 
                      QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)
    
    return win.exec() == QMessageBox.StandardButton.Ok
