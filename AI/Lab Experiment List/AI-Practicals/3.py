import enum
import time


class Action(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Node:
    def __init__(self, state, parent=None, g_score=0):
        self.state = state
        self.parent = parent
        self.g_score = g_score  # Cost from start to current node
        self.h_score = None  # Heuristic estimate of cost to goal
        self.f_score = None  # Total estimated cost (g + h)

    def __lt__(self, other):
        return self.f_score < other.f_score

    def calculate_f_value(self, goal_state):
        # Implement heuristic function here (e.g., number of misplaced tiles)
        self.h_score = self.misplaced_tiles(goal_state)
        self.f_score = self.g_score + self.h_score

    def misplaced_tiles(self, goal_state):
        misplaced = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] != 0 and self.state[i][j] != goal_state[i][j]:
                    misplaced += 1
        return misplaced

    def generate_all_successors(self, empty_tile_pos):
        successors = []
        ROW = len(self.state)
        COL = len(self.state[0])

        # Check for valid moves
        if empty_tile_pos[0] > 0:  # Up
            new_state = self.swap(self.state.copy(), empty_tile_pos, (empty_tile_pos[0] - 1, empty_tile_pos[1]))
            successors.append(Node(new_state, self, self.g_score + 1))
        if empty_tile_pos[0] < ROW - 1:  # Down
            new_state = self.swap(self.state.copy(), empty_tile_pos, (empty_tile_pos[0] + 1, empty_tile_pos[1]))
            successors.append(Node(new_state, self, self.g_score + 1))
        if empty_tile_pos[1] > 0:  # Left
            new_state = self.swap(self.state.copy(), empty_tile_pos, (empty_tile_pos[0], empty_tile_pos[1] - 1))
            successors.append(Node(new_state, self, self.g_score + 1))
        if empty_tile_pos[1] < COL - 1:  # Right
            new_state = self.swap(self.state.copy(), empty_tile_pos, (empty_tile_pos[0], empty_tile_pos[1] + 1))
            successors.append(Node(new_state, self, self.g_score + 1))
        return successors

    def swap(self, state, pos1, pos2):
        state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
        return state


class AstarSearch:
    def __init__(self, initial_state, goal_state):
        self.openlist = [initial_state]
        self.closedlist = []
        self.goal_state = goal_state

    def perform_algorithm(self):
        start_time = time.time()
        goal_node = self.perform_astar_search()
        end_time = time.time()
        return goal_node, (end_time - start_time) * 1000  # Time in milliseconds

    def perform_astar_search(self):
        while self.openlist:
            self.openlist.sort()  # Sort based on f-value
            current_node = self.openlist.pop(0)
            self.closedlist.append(current_node)

            if current_node == self.goal_state:
                return current_node

            empty_tile_pos = self.find_empty_tile(current_node.state)
            child_list = current_node.generate_all_successors(empty_tile_pos)
            for child in child_list:
                child.calculate_f_value(self.goal_state)
                if child not in self.openlist + self.closedlist:
                    self.openlist.append(child)
                elif child in self.openlist:
                    index = self.openlist.index(child)
                    existing_node = self.openlist[index]
                    if child.f_score < existing_node.f_score:
                        self.openlist[index] = child

        return None  # Goal not found

    def final_output(self, goal_node, execution_time):
        if goal_node:
            path = self.get_path(goal_node)
            print("Solution steps:")
            self.print_path(path)
            print("\nNumber of steps:", len(path) - 1)
            print("Execution time:", execution_time, "milliseconds")
        else:
            print("Solution not found.")

    def get_path(self, goal_node):
        path = []
        current = goal_node
        while current:
            path.append(current.state)
            current = current.parent
        path.reverse()
        return path

    def print_path(self, path):
        for i, state in enumerate(path):
            print(f"\nStep {i+1}:")
            print(str(state).replace("],", "]\n"))

    def find_empty_tile(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return (i, j)


if __name__ == "__main__":
    initial_state = []
    goal_state = []

    ROW = 3
    COL = 3

    print("Enter initial state (row by row):")
    for i in range(ROW):
        initial_state.append(list(map(int, input().split())))

    print("Enter goal state (row by row):")
    for i in range(ROW):
        goal_state.append(list(map(int, input().split())))

    search = AstarSearch(initial_state, goal_state)
    goal_node, execution_time = search.perform_algorithm()

    search.final_output(goal_node, execution_time)
