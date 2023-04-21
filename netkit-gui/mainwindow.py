# This Python file uses the following encoding: utf-8
import sys
import os
import json
import matplotlib.pyplot as plt

from dataclasses import dataclass, field
from typing import List
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from ui_form import Ui_MainWindow
from ui_export_dialog import Ui_Dialog as Ui_Export_Dialog
from graphing import *


@dataclass
class Interface:
    name: str = ""
    lan: str = ""
    ip_addr: str = ""
    mask: str = ""
    
    def __repr__(self):
        return {
            "name": self.name,
            "lan": self.lan,
            "ip_addr": self.ip_addr,
            "mask": self.mask
        }


@dataclass
class Machine:
    name: str = ""
    interfaces: List[Interface] = field(default_factory=list)
    custom_startup: str = ""
    
    def __repr__(self):
        return {
            "name": self.name,
            "custom_startup": self.custom_startup,
            "interfaces": [
                i.__repr__() for i in self.interfaces
            ]
        }
        
        
class Export_Dialog(QDialog, Ui_Export_Dialog):
    def __init__(self, parent: 'MainWindow'):
        super().__init__()
        self.setupUi(self)
        
        self.mainwindow = parent
        self.buttonBox.accepted.connect(self.__export_hook)
        
    def __export_hook(self):
        # TODO: Validation
        path = self.dir_edit.text()
        os.makedirs(path, exist_ok=True)
        
        # Machine files/dirs
        for m in self.mainwindow.machines:
            with open(os.path.join(path, m.name + ".startup"), "w") as f:
                f.write(self.make_startup(m))
                
            os.mkdir(os.path.join(path, m.name))
        
        # lab.conf
        with open(os.path.join(path, "lab.conf"), "w") as f:
            for m in self.mainwindow.machines:
                for i in m.interfaces:
                    f.write(f"{m.name}[{i.name}]={i.lan}\n")
                    
        # Close
        self.close()
            
    @staticmethod
    def make_startup(machine: Machine) -> str:
        s = ""
        
        for i in machine.interfaces:
            s += f"ip a add {i.ip_addr} dev {i.name} \t# LAN: {i.lan}\n"
            s += f"ip link set up dev {i.name}\n"
            
        s += machine.custom_startup
        
        return s


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.current_machine_index = -1
        self.current_if_index = -1
        
        # Load Machines
        self.machines: List[Machine] = []
        
        if not os.path.exists("netkit-lab.json"):
            with open("netkit-lab.json", "w") as f:
                f.write("[]")
                            
        with open("netkit-lab.json") as f:
            for m in json.load(f):
                machine = Machine(
                    m["name"], custom_startup=m["custom_startup"]
                )
                
                for i in m["interfaces"]:
                    machine.interfaces.append(Interface(
                        i["name"], i["lan"], i["ip_addr"], i["mask"]
                    ))
                    
                self.machines.append(machine)
                
        self.__update_machine_list()
        
        # Hooks
        self.ui.update_button.clicked.connect(self.__update_machine_hook)
        self.ui.new_machine_button.clicked.connect(self.__new_machine_hook)
        self.ui.delete_machine_button.clicked.connect(self.__delete_machine_hook)
        self.ui.machine_list.clicked.connect(self.__change_machine_hook)
        
        self.ui.update_if_button.clicked.connect(self.__update_interface_hook)
        self.ui.delete_if_button.clicked.connect(self.__delete_interface_hook)
        self.ui.new_if_button.clicked.connect(self.__new_interface_hook)
        self.ui.interfaces.clicked.connect(self.__change_interface_hook)
        
        self.ui.graph_button.clicked.connect(self.__graph_hook)
        self.ui.export_button.clicked.connect(self.__export_hook)
        
    def __clear_machine_data(self):
        self.ui.machine_name_edit.setText("")
        self.ui.startup_edit.setPlainText("")
        self.__clear_if_data()
                
    def __update_machine_list(self):
        self.ui.machine_list.clear()
        
        for m in self.machines:
            self.ui.machine_list.addItem(m.name)

    def __update_machine_hook(self):
        if self.current_machine_index >= 0:
            # TODO: Check inputs
            m = self.machines[self.current_machine_index]
            m.name = self.ui.machine_name_edit.text()
            m.custom_startup = self.ui.startup_edit.toPlainText()
        
            self.__update_machine_list()
            
    def __new_machine_hook(self):
        self.machines.append(Machine())
        self.current_machine_index = len(self.machines) - 1
        
        self.ui.machine_name_edit.setText("")
        self.ui.startup_edit.setPlainText("")
        self.current_if_index = -1
        self.__clear_if_data()
        self.ui.interfaces.clear()
        
    def __delete_machine_hook(self):
        if self.current_machine_index >= 0:
            self.machines.pop(self.current_machine_index)
            self.current_machine_index = -1
            
            self.__clear_machine_data()
            self.__update_machine_list()
            
    def __change_machine_hook(self):
        self.current_machine_index = self.ui.machine_list.currentIndex().row()
        
        m = self.machines[self.current_machine_index]
        self.ui.machine_name_edit.setText(m.name)
        self.ui.startup_edit.setPlainText(m.custom_startup)
        
        self.__update_if_list()
        self.__clear_if_data()
            
    def __clear_if_data(self):
        self.ui.interface_name_edit.setText("")
        self.ui.lan_name_edit.setText("")
        self.ui.ip_address_edit.setText("")
        self.ui.netmask_edit.setText("")
        
    def __update_if_list(self):
        self.ui.interfaces.clear()
        
        if self.current_machine_index >= 0:
            for i in self.machines[self.current_machine_index].interfaces:
                self.ui.interfaces.addItem(i.name)

    def __update_interface_hook(self):
        if self.current_if_index >= 0:
            # TODO: Check inputs
            i = self.machines[self.current_machine_index].interfaces[self.current_if_index]
            i.name = self.ui.interface_name_edit.text()
            i.lan = self.ui.lan_name_edit.text()
            i.ip_addr = self.ui.ip_address_edit.text()
            i.mask = self.ui.netmask_edit.text()
            
            self.__update_if_list()
            
    def __delete_interface_hook(self):
        if self.current_if_index >= 0:
            self.machines[self.current_machine_index].interfaces.pop(self.current_if_index)
            self.current_if_index = -1
        
            self.__clear_if_data()
            self.__update_if_list()
            
    def __change_interface_hook(self):
        self.current_if_index = self.ui.interfaces.currentIndex().row()
        
        i = self.machines[self.current_machine_index].interfaces[self.current_if_index]
        self.ui.interface_name_edit.setText(i.name)
        self.ui.lan_name_edit.setText(i.lan)
        self.ui.ip_address_edit.setText(i.ip_addr)
        self.ui.netmask_edit.setText(i.mask)
            
    def __new_interface_hook(self):
        if self.current_machine_index >= 0:
            self.machines[self.current_machine_index].interfaces.append(Interface())
            self.current_if_index = len(self.machines[self.current_machine_index].interfaces) - 1
            
            self.__clear_if_data()
            
    def __graph_hook(self):
        graph = Graph()
        graph.load_machines(self.machines)
        
        networkx.drawing.nx_pylab.draw(graph, 
            node_color=[n[1]["color"] for n in graph.nodes(data=True)],
            with_labels=True
        )
        
        plt.show()
        
    def __export_hook(self):
        dialog = Export_Dialog(self)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    
    code = app.exec()

    # Exited
    with open("netkit-lab.json", "w") as f:
        json.dump([m.__repr__() for m in widget.machines], f)
        
    sys.exit(code)
