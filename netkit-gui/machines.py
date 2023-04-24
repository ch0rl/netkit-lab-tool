import os
import json

from _dataclasses import *
from ui_form import Ui_MainWindow
from interfaces import Interface_Handler
from errors import show_err


class Machine_Handler:
    def __init__(self, ui: Ui_MainWindow, if_handler: Interface_Handler, 
                 path_to_json: str | None = None):
        
        self.ui = ui
        self.if_handler = if_handler
        
        self.machines: List[Machine] = []
        if path_to_json is not None:
            self.path = path_to_json
            self.load_from_file(path_to_json)
        else:
            self.path = "netkit-lab.json"
            
        self.current_machine: Machine | None = None
        
    def load_from_file(self, path: str):
        # Check path exists
        if not os.path.exists(path):
            show_err("Path Error", f"Path '{path}' does not exist")            
            self.ui.close()
        
        with open(path) as f:
            for m in json.load(f):
                machine = Machine(
                    m["name"], custom_startup=m["custom_startup"]
                )
                
                for i in m["interfaces"]:
                    machine.interfaces.append(Interface(
                        i["name"], i["lan"], i["ip_addr"], i["mask"]
                    ))
                    
                self.machines.append(machine)
        
    def set_read_only(self, state: bool):
        self.ui.machine_name_edit.setReadOnly(state)
        self.ui.startup_edit.setReadOnly(state)
        
    def clear(self):
        self.ui.machine_name_edit.setText("")
        self.ui.startup_edit.setPlainText("")
        
        self.if_handler.clear()

    def update_list(self):
        self.ui.machine_list.clear()
        
        for m in self.machines:
            self.ui.machine_list.addItem(m.name)
            
    def save_changes(self) -> bool:
        if self.current_machine is not None:
            # Can't have duplicate machine names
            name = self.ui.machine_name_edit.text()
            if any(x.name == name and x != self.current_machine for x in self.machines):
                show_err("Duplicate Name", f"A machine with name '{name}' already exists.")
                
                return False
            else:
                self.current_machine.name = name
                self.current_machine.custom_startup = self.ui.startup_edit.toPlainText()
                
                self.update_list()
                
                return True
        else:
            # Saving to no current machine is valid
            return True
            
    def new(self):
        self.machines.append(Machine(name="unnamed"))
        self.change(len(self.machines) - 1)
        self.update_list()
        
    def update_displayed(self):
        if self.current_machine is not None:
            self.ui.machine_name_edit.setText(self.current_machine.name)
            self.ui.startup_edit.setPlainText(self.current_machine.custom_startup)
            
            self.if_handler.update_displayed()
        else:
            self.clear()
            
    def delete_current(self):
        if self.current_machine is not None:
            self.machines.remove(self.current_machine)
            self.current_machine = None
            
            self.if_handler.change_machine(None)
            
            self.update_displayed()
            self.update_list()
            self.if_handler.update_list()
            
            self.set_read_only(True)
            
    def change(self, new_index: int):
        if self.save_changes():
            self.if_handler.clear()
            
            self.current_machine = self.machines[new_index]
            self.if_handler.change_machine(self.current_machine)
            
            self.update_displayed()
            self.if_handler.update_list()
            
            self.set_read_only(False)
            self.if_handler.set_read_only(True)
