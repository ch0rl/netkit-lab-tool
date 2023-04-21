import networkx
from typing import List
from mainwindow import Machine


class Graph(networkx.Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def load_machines(self, machines: List[Machine]):
        # Make lans
        lans = set()
        for m in machines:
            for i in m.interfaces:
                lans.add(f"LAN: {i.lan}")
        
        self.add_nodes_from(lans, color="white")
        
        # Connect machines
        for m in machines:
            self.add_node(m.name, color="grey")
            
            for i in m.interfaces:
                self.add_edge(m.name, f"LAN: {i.lan}")
