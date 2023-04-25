from pyvis.network import Network
from typing import List

from _dataclasses import *

class Graph(Network):
    def __init__(self, *args, **kwargs):
        """A subclass of pyvis.network.Network to handle machines
        
        Args:
            *args, **kwargs: [keyword] arguments to pass to super().__init__
        """
        
        super().__init__(*args, **kwargs)
        
        # Add the physics options
        self.show_buttons(filter_="physics")
        
    def load_machines(self, machines: List[Machine]):
        """Loads a list of machines into the graph
        
        Args:
            machines: the list of machines to load in
        """
        
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
