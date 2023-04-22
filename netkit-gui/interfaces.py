from ui_form import Ui_MainWindow
from _dataclasses import *

class Interface_Handler:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        
        self.current_machine: Machine | None = None
        self.current_if: Interface | None = None
        
    def set_read_only(self, state: bool):
        self.ui.interface_name_edit.setReadOnly(state)
        self.ui.lan_name_edit.setReadOnly(state)
        self.ui.ip_address_edit.setReadOnly(state)
        self.ui.netmask_edit.setReadOnly(state)
        
    def change_machine(self, new: Machine | None):
        self.current_if = None
        self.current_machine = new
        
    def clear(self):
        self.ui.interface_name_edit.setText("")
        self.ui.lan_name_edit.setText("")
        self.ui.ip_address_edit.setText("")
        self.ui.netmask_edit.setText("")

    def update_list(self):
        if self.current_machine is not None:
            self.ui.interfaces.clear()
            
            for m in self.current_machine.interfaces:
                self.ui.interfaces.addItem(m.name)
            
    def save_changes(self):
        if self.current_if is not None:
            self.current_if.name = self.ui.interface_name_edit.text()
            self.current_if.lan = self.ui.lan_name_edit.text()
            self.current_if.ip_addr = self.ui.ip_address_edit.text()
            self.current_if.mask = self.ui.netmask_edit.text()
            
            self.update_list()
            
    def new(self):
        if self.current_machine is not None:
            self.save_changes()
            
            self.current_if = Interface(name="unnamed")
            self.current_machine.interfaces.append(self.current_if)
            
            self.update_displayed()
            self.update_list()
            
            self.set_read_only(False)
        
    def update_displayed(self):
        if self.current_if is not None:
            self.ui.interface_name_edit.setText(self.current_if.name)
            self.ui.lan_name_edit.setText(self.current_if.lan)
            self.ui.ip_address_edit.setText(self.current_if.ip_addr)
            self.ui.netmask_edit.setText(self.current_if.mask)
        else:
            self.clear()
            
    def delete_current(self):
        if self.current_if is not None and self.current_machine is not None:
            self.current_machine.interfaces.remove(self.current_if)
            self.current_if = None
            
            self.update_displayed()
            self.update_list()
            
            self.set_read_only(True)
            
    def change(self, new_index: int):
        if self.current_machine is not None:
            self.save_changes()
            
            # TODO: Validation
            self.current_if = self.current_machine.interfaces[new_index]
            
            self.update_displayed()
            self.set_read_only(False)
