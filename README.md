# tkinter_tsp
The minimal visualization version with Tkinter for apply algorithms on TSP (Python)
# who is this for
I wrote this script for visualization the algorithms on my school project!
For students mostly!
# Following rules
#You should named the attribute of class Node like below
```python
class Node:
    def __init__(self, name, latitude, longtitude):
      self.name = name
      self.y = latitude
      self.x = longtitude
```
#The algorithm choice must return the list of Node object
# Usage
```python
from RouteVisualizer import *
window = Window()
window.addNodes(node_list)
window.addAlgo({"2-opt": .<function address>., "NearestNeighbor": .<function address>.)
window.run()
```
# Customization your keyboard action binding
```python
class KEYBIND:
    zoomin = "z"
    zoomout = "x"
    up = "w"
    down = "s"
    left = "a"
    right = "d"
    revert = '-'
    deploy = '+'
```
# !
the file RouteVisualizer.py is all what you need. I added others file just for testing purposes. (just proof of concept) .
You can modify it to match your previous implementation. ^ ^
my code usage :
```bash
./tsp.py vn_cities.csv
```
# That's it !
