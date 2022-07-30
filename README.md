# Algorithm description
The implemented greedy algorithm uses a heuristic based on the randomization of the turning direction to adapt to any type of map. At the beginning a direction is selected and followed until it collides with an obstacle. Subsequently another direction is selected, if there is no obstacle and it is not a visited path it follows that direction until it collides again. When there is no free path, it returns to the previous node and checks if it has any free direction, else it continues iterating in the previous nodes.

# Results

The greedy algorithm proves to be in general faster than BFS in most situations. However, it does not usually find the optimal path. This is especially evident when the map haa a square shape and the algorithm performs spiral paths. To avoid that, it would be convenient to apply a node search algorithm such as Dijsktra or A* after having reached the goal to trace the final path.

# Notes
- A graphical interface has been made to display the maps comfortably on the terminal. Screen wipe is compatible with windows and linux. The refresh rate is modified with the variable "DISPLAY_TIME"
- The final route is represented on the map when the goal is found
- Maps and algorithms are selected in the terminal. Start and end points are loaded via a dictionary. Errors in entering selection numbers are avoided.
- The computation time of each algorithm is calculated.
- Video: https://youtu.be/eMjHF4yqs44

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/eMjHF4yqs44/0.jpg)](https://youtu.be/eMjHF4yqs44)
