import time

class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Node:
    def __init__(self, state, parent, action, depth, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost
        self.priority = depth + cost

    def __lt__(self, other):
        return self.priority < other.priority

    def expand(self):
        children = []
        x, y = self.find_blank_tile()
        if x > 0:
            children.append(self.move(x, y, x - 1, y, Action.UP))
        if x < 2:
            children.append(self.move(x, y, x + 1, y, Action.DOWN))
        if y > 0:
            children.append(self.move(x, y, x, y - 1, Action.LEFT))
        if y < 2:
            children.append(self.move(x, y, x, y + 1, Action.RIGHT))
        return children

    def move(self, x1, y1, x2, y2, action):
        new_state = [list(row) for row in self.state]
        new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
        return Node(tuple(tuple(row) for row in new_state), self, action, self.depth + 1, 0)

    def find_blank_tile(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

class AStarSearch:
    def __init__(self, initial_state, goal_state):
        self.open_list = [initial_state]
        self.closed_list = set()
        self.goal_state = goal_state

    def perform_algorithm(self):
        while self.open_list:
            current_node = min(self.open_list)
            self.open_list.remove(current_node)
            self.closed_list.add(current_node.state)

            if current_node.state == self.goal_state:
                return current_node

            for child in current_node.expand():
                if child.state not in self.closed_list:
                    self.open_list.append(child)

        return None

def print_path(solution_node):
    path = []
    current_node = solution_node
    while current_node:
        path.append(current_node.state)
        current_node = current_node.parent
    path.reverse()
    for state in path:
        print_state(state)
        print()

def print_state(state):
    for row in state:
        print(row)
    print()

def get_user_input():
    print("Enter the initial state of the 8-puzzle (3x3 grid, use 0 to represent the blank tile):")
    initial_state = []
    for i in range(3):
        row = input(f"Enter values for row {i + 1} separated by space: ").strip().split()
        initial_state.append([int(num) for num in row])

    print("Enter the goal state of the 8-puzzle (3x3 grid, use 0 to represent the blank tile):")
    goal_state = []
    for i in range(3):
        row = input(f"Enter values for row {i + 1} separated by space: ").strip().split()
        goal_state.append([int(num) for num in row])

    return initial_state, goal_state

if __name__ == "__main__":
    initial_state, goal_state = get_user_input()
    start_time = time.time()
    initial_node = Node(tuple(tuple(row) for row in initial_state), None, None, 0, 0)
    goal_node = Node(tuple(tuple(row) for row in goal_state), None, None, 0, 0)
    astar = AStarSearch(initial_node, goal_node)
    solution_node = astar.perform_algorithm()
    end_time = time.time()

    if solution_node:
        print("Solution Found!")
        print("Path to goal state:")
        print_path(solution_node)
        print(f"Execution Time: {(end_time - start_time) * 1000} milliseconds")
    else:
        print("No solution found.")
