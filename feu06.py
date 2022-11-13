import sys
import heapq
import math

class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(maze, start, end, allow_diagonal_movement = True):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len(maze[0]) * len(maze) // 2)

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you find the end
    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
          # if we hit this point return the path such as it is
          # it will not contain the destination
          warn("giving up on pathfinding too many iterations")
          return return_path(current_node)       
        
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []
        
        for new_position in adjacent_squares: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    warn("Couldn't get a path to destination")
    return None


def getMapString(file):
    L= []
    with open(file,"r") as f:
        [L.append(list(line.replace("\n", "").replace(" ","-").strip())) for line in f.readlines()]
    return L

def getMap(file):
    L= getMapString(file)
    enter = -1
    out = []
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "1" : enter = (i,j)
            if L[i][j] == "2" : out.append((i,j)) 
            if L[i][j] == " " or L[i][j] == "2" or L[i][j] == "1" or L[i][j] == "-" : L[i][j] = 0
            else : L[i][j] = 1
    return L[:],enter,out

def printMap(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0 :
                print(" ",end="")
            if map[i][j] == 1 :
                print("*",end="")
            if map[i][j] == 3 :
                print("°",end="")
            if map[i][j] == 4 :
                print("1",end="")
            if map[i][j] == 5 :
                print("2",end="")
        print("")

def addPath(map,path,enter,out):
    for i in path:
        map[i[0]][i[1]] = 3
    map[enter[0]][enter[1]] = 4
    for k in out:
        map[k[0]][k[1]] = 5

def lowestPath(paths):
    min_len = math.inf
    best_path = None
    for path in paths :
        if len(path) < min_len:
            min_len = len(path)
            best_path = path
    return best_path


try :
    if len(sys.argv) != 2:
        raise Exception
    file=sys.argv[1]
    map,enter,out = getMap(file)
    paths = []
    for outter in out:
        paths.append(astar(map, enter, outter))
    lowest_path = lowestPath(paths)
    addPath(map, lowest_path,enter,out)
    printMap(map)
    print(f"=> SORTIE ATTEINTE EN {len(lowest_path)} COUPS !")
except Exception as e:
    print("erreur.",e)

        
    

