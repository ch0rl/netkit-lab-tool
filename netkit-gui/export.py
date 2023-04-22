import os
import json

from PySide6.QtWidgets import QDialog
from ui_export_dialog import Ui_Dialog as Ui_Export_Dialog

from _dataclasses import *


class Export_Dialog(QDialog, Ui_Export_Dialog):
    def __init__(self, machines: List[Machine],  save_lab=False):
        super().__init__()
        self.setupUi(self)
        
        self.machines = machines
        
        if save_lab:
            self.buttonBox.accepted.connect(self.__save_hook)
        else:
            self.buttonBox.accepted.connect(self.__export_hook)
        
    def __export_hook(self):
        # TODO: Validation
        path = self.dir_edit.text()
        os.makedirs(path, exist_ok=True)
        
        # Machine files/dirs
        for m in self.machines:
            with open(os.path.join(path, m.name + ".startup"), "w") as f:
                f.write(self.make_startup(m))
                
            os.mkdir(os.path.join(path, m.name))
        
        # lab.conf
        with open(os.path.join(path, "lab.conf"), "w") as f:
            for m in self.machines:
                for i in m.interfaces:
                    f.write(f"{m.name}[{i.name}]={i.lan}\n")
                    
        # Close
        self.close()
        
    def __save_hook(self):
        # TODO: Validation
        path = self.dir_edit.text()
        os.makedirs(path, exist_ok=True)
        
        with open(os.path.join(path, "netkit-lab.json"), "w") as f:
            json.dump([m.__repr__() for m in self.machines], f)
            
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
