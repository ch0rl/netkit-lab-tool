import re

from errors import warn_ask, show_err
from _dataclasses import *
from patterns import *

class Interface_Handler:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        
        self.current_machine: Machine | None = None
        self.current_if: Interface | None = None
        
    def set_read_only(self, state: bool):
        self.mainwindow.ui.interface_name_edit.setReadOnly(state)
        self.mainwindow.ui.lan_name_edit.setReadOnly(state)
        self.mainwindow.ui.ip_address_edit.setReadOnly(state)
        self.mainwindow.ui.netmask_edit.setReadOnly(state)
        
    def change_machine(self, new: Machine | None):
        self.current_if = None
        self.current_machine = new
        
    def clear(self):
        self.mainwindow.ui.interface_name_edit.setText("")
        self.mainwindow.ui.lan_name_edit.setText("")
        self.mainwindow.ui.ip_address_edit.setText("")
        self.mainwindow.ui.netmask_edit.setText("")

    def update_list(self):
        if self.current_machine is not None:
            self.mainwindow.ui.interfaces.clear()
            
            for m in self.current_machine.interfaces:
                self.mainwindow.ui.interfaces.addItem(m.name)
            
    def save_changes(self) -> bool:
        if self.current_if is not None:
            # Warn about same IP on same LAN
            # Note: this is quite compute-heavy so maybe don't?
            ip_addr = self.mainwindow.ui.ip_address_edit.text()
            lan = self.mainwindow.ui.lan_name_edit.text()
            for m in self.mainwindow.machines.machines:
                if m == self.current_machine: continue
                for i in m.interfaces:
                    if i.lan == lan and i.ip_addr == ip_addr:
                        if not warn_ask(
                            "IP Clash", f"Machine '{m.name}', on lan '{lan}', already has the IP '{ip_addr}' - on interface '{i.name}'."
                        ):
                            return False
            
            name = self.mainwindow.ui.interface_name_edit.text()
            mask = self.mainwindow.ui.netmask_edit.text()
            
            # Input Validation
            for p, v in (
                (IP_PATTERN, ip_addr),
                (NAME_PATTERN, lan),
                (NAME_PATTERN, name),
                (MASK_PATTERN, mask)
            ):
                if re.match(p, v) is None:
                    show_err("Validation Error", f"Input '{v}' does not match pattern '{p}'.")
                    return False
            
            self.current_if.name = name
            self.current_if.lan = lan
            self.current_if.ip_addr = ip_addr
            self.current_if.mask = mask
            
            self.update_list()
            
            return True
        else:
            # Updating with no interface is valid
            return True
            
    def new(self):
        if self.current_machine is not None:
            if self.save_changes():
                self.current_if = Interface(name="unnamed")
                self.current_machine.interfaces.append(self.current_if)
                
                self.update_displayed()
                self.update_list()
                
                self.set_read_only(False)
        
    def update_displayed(self):
        if self.current_if is not None:
            self.mainwindow.ui.interface_name_edit.setText(self.current_if.name)
            self.mainwindow.ui.lan_name_edit.setText(self.current_if.lan)
            self.mainwindow.ui.ip_address_edit.setText(self.current_if.ip_addr)
            self.mainwindow.ui.netmask_edit.setText(self.current_if.mask)
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
            if self.save_changes():
                # TODO: Validation
                self.current_if = self.current_machine.interfaces[new_index]
                
                self.update_displayed()
                self.set_read_only(False)
