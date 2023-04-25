import os
import re
import json

from _dataclasses import *
from interfaces import Interface_Handler
from errors import show_err
from patterns import *


class Machine_Handler:
    def __init__(self, mainwindow, if_handler: Interface_Handler, 
                 path_to_json: str | None = None):
        
        """A class to handle interactions with machines
        
        Args:
            mainwindow: the mainwindow.MainWindow object that uses this handler
            if_handler: the interfaces.Interface_Handler object in use
            path_to_json: the path to the JSON file of the lab
        """
        
        self.mainwindow = mainwindow
        self.if_handler = if_handler
        
        self.machines: List[Machine] = []
        if path_to_json is not None:
            self.path = path_to_json
            self.load_from_file(path_to_json)
        else:
            self.path = "netkit-lab.json"
            
        self.current_machine: Machine | None = None
        
    def load_from_file(self, path: str):
        """Loads machines from a lab file
        
        Args:
            path: the path to the JSON file
        """
        
        # Check path exists
        if not os.path.exists(path):
            show_err("Path Error", f"Path '{path}' does not exist")            
            self.mainwindow.close()
            
        with open(path) as f:
            try:
                for m in json.load(f):
                    # Validate and load machine info
                    if "name" not in m or "custom_startup" not in m or "interfaces" not in m:
                        show_err("Invalid JSON", 
                                 f"""Machine '{json.dumps(m)}' must have "name", "custom_startup", and "interfaces".""")
                        self.mainwindow.close()
                    
                    machine = Machine(
                        m["name"], custom_startup=m["custom_startup"]
                    )
                    
                    # Validate and load interfaces
                    for i in m["interfaces"]:
                        if "name" not in i or "lan" not in i or "ip_addr" not in i or "mask" not in i:
                            show_err("Invalid JSON", 
                                     f"""Interface '{json.dumps(i)}' must have "name", "lan", "ip_addr", and "mask".""")
                            self.mainwindow.close()
                        
                        machine.interfaces.append(Interface(
                            i["name"], i["lan"], i["ip_addr"], i["mask"]
                        ))
                        
                    self.machines.append(machine)
                    
            except json.JSONDecodeError as e:
                # Show error then close
                show_err("JSON Decode Error", e.msg)
                self.mainwindow.close()
        
    def set_read_only(self, state: bool):
        """Sets machine inputs' read-only state
        
        Args:
            state: the state to set
        """
        
        self.mainwindow.ui.machine_name_edit.setReadOnly(state)
        self.mainwindow.ui.startup_edit.setReadOnly(state)
        
    def clear(self):
        """Sets all machine inputs to an empty string"""
        
        self.mainwindow.ui.machine_name_edit.setText("")
        self.mainwindow.ui.startup_edit.setPlainText("")
        
        self.if_handler.clear()

    def update_list(self):
        """Updates the displayed list of machines to represent the stored list"""
        
        self.mainwindow.ui.machine_list.clear()
        
        for m in self.machines:
            self.mainwindow.ui.machine_list.addItem(m.name)
            
    def save_changes(self) -> bool:
        """Saves inputted values to the current machine
        
        Returns:
            bool: whether the save worked or not (ie., if tests passed)
        """
        
        if self.current_machine is not None:
            # Can't have duplicate machine names
            name = self.mainwindow.ui.machine_name_edit.text()
            if any(x.name == name and x != self.current_machine for x in self.machines):
                show_err("Duplicate Name", f"A machine with name '{name}' already exists.")
                
                return False
            else:
                # Input validation
                if re.match(NAME_PATTERN, name) is None:
                    show_err("Validation Error", f"Input '{name}' does not match pattern '{NAME_PATTERN}'.")
                    return False
                
                self.current_machine.name = name
                self.current_machine.custom_startup = self.mainwindow.ui.startup_edit.toPlainText()
                
                self.update_list()
                
                return True
        else:
            # Saving to no current machine is valid
            return True
            
    def new(self):
        """Creates a new machine, adds it to the list, and switches to it"""
        
        self.machines.append(Machine(name="unnamed"))
        self.change(len(self.machines) - 1)
        self.update_list()
        
    def update_displayed(self):
        """Updates the displayed values to represent the current machine"""
        
        if self.current_machine is not None:
            self.mainwindow.ui.machine_name_edit.setText(self.current_machine.name)
            self.mainwindow.ui.startup_edit.setPlainText(self.current_machine.custom_startup)
            
            self.if_handler.update_displayed()
        else:
            self.clear()
            
    def delete_current(self):
        """Deletes the current machine"""
        
        if self.current_machine is not None:
            self.machines.remove(self.current_machine)
            self.current_machine = None
            
            self.if_handler.change_machine(None)
            
            self.update_displayed()
            self.update_list()
            self.if_handler.update_list()
            
            self.set_read_only(True)
            
    def change(self, new_index: int):
        """Changes the current machine to that at new_index
        
        Args:
            new_index: the index of the new interface
        """
        
        if self.save_changes():
            self.if_handler.clear()
            
            self.current_machine = self.machines[new_index]
            self.if_handler.change_machine(self.current_machine)
            
            self.update_displayed()
            self.if_handler.update_list()
            
            self.set_read_only(False)
            self.if_handler.set_read_only(True)
