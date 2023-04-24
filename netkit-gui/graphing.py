from pyvis.network import Network
from typing import List

from _dataclasses import *

class Graph(Network):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_buttons(filter_="physics")
        
    def load_machines(self, machines: List[Machine]):
        # Make lans
        lans = set()
        for m in machines:
            for i in m.interfaces:
                lans.add(f"LAN: {i.lan}")
        
        lans = list(lans)
        self.add_nodes(lans, title=lans, color=["white"] * len(lans))
        
        # Connect machines
        for m in machines:
            self.add_node(m.name, label=m.name, color="grey")
            
            for i in m.interfaces:
                self.add_edge(m.name, f"LAN: {i.lan}")
