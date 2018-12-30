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
#The algorithm choice must have the SAME INPUT and OUPUT type.
# Usage
```python
from RouteVisualizer import *
window = Window()
# add initial origin data first
window.addNodes(graph.Nodes)
window.addAlgoChoice('2opt', LocalSearch.Opt2Solve, graph.Nodes,  returnid = 0)
#                    name ,  func_address,   *arguments,    returnid 
#                    "returnid" : indicate which argument[id] of the arugument will be displayed (must has type : list of Nodes)
window.addAlgoChoice('GA',GA._Evolving, pop, GA.bestGene, returnid = 1)
#                         GA._Evolving (pop, gene) <-- signature of function
#                         take the "1"th index of arugment to draw on screen: (GA.bestGene)
#                         we only care about the "1th" arugment(count from 0) to be displayed
window.run()
```
window.addAlgoChoice(name, func_address, *argument, returnid)
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
