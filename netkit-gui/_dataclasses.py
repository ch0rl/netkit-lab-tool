from dataclasses import dataclass, field
from typing import List


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
            "mask": self.mask,
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
            "interfaces": [i.__repr__() for i in self.interfaces],
        }
