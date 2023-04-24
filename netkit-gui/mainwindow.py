# This Python file uses the following encoding: utf-8
import sys
import json

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow

from graphing import *
from _dataclasses import *

from export import Export_Dialog

from machines import Machine_Handler
from interfaces import Interface_Handler


class MainWindow(QMainWindow):
    def __init__(self, parent=None, path_to_json: str | None = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.interfaces = Interface_Handler(self.ui)
        self.machines = Machine_Handler(self, self.interfaces, path_to_json)
        self.machines.update_list()
        
        self.machines.set_read_only(True)
        self.interfaces.set_read_only(True)
        
        # Hooks
        self.ui.update_button.clicked.connect(self.machines.save_changes)
        self.ui.new_machine_button.clicked.connect(self.machines.new)
        self.ui.delete_machine_button.clicked.connect(self.machines.delete_current)
        self.ui.machine_list.currentRowChanged.connect(self.__change_machine_hook)
        
        self.ui.update_if_button.clicked.connect(self.interfaces.save_changes)
        self.ui.new_if_button.clicked.connect(self.interfaces.new)
        self.ui.delete_if_button.clicked.connect(self.interfaces.delete_current)
        self.ui.interfaces.currentRowChanged.connect(self.__change_if_hook)
        
        self.ui.graph_button.clicked.connect(self.__graph_hook)
        self.ui.export_button.clicked.connect(self.__export_hook)
        self.ui.save_button.clicked.connect(self.__save_hook)
            
    def __graph_hook(self):
        graph = Graph(select_menu=True, filter_menu=True)
        graph.load_machines(self.machines.machines)
        graph.show("NetworkGraph.html", notebook=False)
        
    def __export_hook(self):
        dialog = Export_Dialog(self.machines.machines)
        dialog.exec()
        
    def __save_hook(self):
        dialog = Export_Dialog(self.machines.machines, True)
        dialog.exec()
        
    def __change_machine_hook(self):
        self.machines.change(self.ui.machine_list.currentRow())
        
    def __change_if_hook(self):
        self.interfaces.change(self.ui.interfaces.currentRow())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow(path_to_json=sys.argv[1])
    widget.show()
    
    code = app.exec()

    # Exited
    with open("netkit-lab.json", "w") as f:
        json.dump([m.__repr__() for m in widget.machines.machines], f)
        
    sys.exit(code)
