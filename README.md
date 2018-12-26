# tkinter_tsp
The minimal visualization version with Tkinter for apply algorithms on TSP (Python)
# what is this for
Im writing this script for visualization the algorithms on my school project!
for students mostly
# Following rules
#You should named the attribute of class Node like below
class Node:
    def __init__(self, name, latitude, longtitude):
      self.name = name
      self.y = latitude
      self.x = longtitude
#The algorithm choice must return the list of Node object
# Usage
from Route_Visualizer import *
window = Window()
window.addNodes(node_list)
window.addAlgo({"2-opt": .<function address>., "NearestNeighbor": .<function address>.)
window.run()

# That's it
