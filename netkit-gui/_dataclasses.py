from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Interface:
    """A network interface
    
    Attrs:
        name: the name of the interface
        lan: the Netkit lan that this interface connects to
        ip_addr: the IP address associated with this interface
        mask: the (CIDR) network mask associated with the lan this connects to
    """
    
    name: str = ""
    lan: str = ""
    ip_addr: str = ""
    mask: str = ""

    def __repr__(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "lan": self.lan,
            "ip_addr": self.ip_addr,
            "mask": self.mask,
        }


@dataclass
class Machine:
    """A Netkit machine
    
    Attrs:
        name: the (host)name of the machine
        interfaces: a list of the attached network interfaces
        custom_startup: a string to append to the startup file
    """
    
    name: str = ""
    interfaces: List[Interface] = field(default_factory=list)
    custom_startup: str = ""

    def __repr__(self) -> Dict[str, str | List[Dict[str, str]]]:
        return {
            "name": self.name,
            "custom_startup": self.custom_startup,
            "interfaces": [i.__repr__() for i in self.interfaces],
        }
