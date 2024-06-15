from enum import Enum
import time

class Action(Enum):
    MoveUp = 1
    MoveDown = 2
    MoveLeft = 3
    MoveRight = 4
    NoAction = 5

class Node:
    def __init__(self, position=[], parent=None, action=Action.NoAction):
        self.position = position
        self.parent = parent
        self.action = action
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    def isLoop(self):
        current = self
        seen = set()
        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.parent
        return False

    def __eq__(self, other):
        return other is not None and self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        strAction = ""
        if self.action != Action.NoAction:
            strAction = self.action.name

        return '\n'.join([str(strAction), str(self.position[:3]),
                         str(self.position[3:6]), str(self.position[6:9])]).replace('[', '').replace(']', '').replace(',', '').replace('0', 'x')

    def _g(self):
        return self.depth

    def _h(self, goal):
        return sum([1 if self.position[i] != goal[i] else 0 for i in range(9)])

    def calculate_heuristic_value(self, goal):
        self.h = self._h(goal)
        self.g = self._g()
        self.f = self.g + self.h

    def possible_moves(self):
        successors = []
        i = self.position.index(0)

        if i in [3, 4, 5, 6, 7, 8]:
            new_board = self.position[:]
            new_board[i], new_board[i - 3] = new_board[i - 3], new_board[i]
            successors.append(Node(new_board, self, Action.MoveUp))

        if i in [0, 1, 3, 4, 6, 7]:
            new_board = self.position[:]
            new_board[i], new_board[i + 1] = new_board[i + 1], new_board[i]
            successors.append(Node(new_board, self, Action.MoveRight))

        if i in [1, 2, 4, 5, 7, 8]:
            new_board = self.position[:]
            new_board[i], new_board[i - 1] = new_board[i - 1], new_board[i]
            successors.append(Node(new_board, self, Action.MoveLeft))

        if i in [0, 1, 2, 3, 4, 5]:
            new_board = self.position[:]
            new_board[i], new_board[i + 3] = new_board[i + 3], new_board[i]
            successors.append(Node(new_board, self, Action.MoveDown))

        return successors

def a_star_search(start, end):
    open_list = []
    closed = []
    start_node = Node(start, None)
    goal_node = Node(end, None)
    open_list.append(start_node)

    while len(open_list) > 0:
        open_list.sort()
        current_node = open_list.pop(0)
        closed.append(current_node)

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = current_node.parent
            path.append(start_node)
            return path[::-1]

        neighbors = current_node.possible_moves()

        for neighbor in neighbors:
            if neighbor in closed:
                continue
            neighbor.calculate_heuristic_value(end)
            if can_add_to_open(open_list, neighbor):
                open_list.append(neighbor)

    return None

def can_add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node:
            if neighbor.f >= node.f:
                return False
            else:
                open_list.remove(node)
                return True
    return True

print("Adeshara Brijesh:")
print("21012021001")
def main():
    start = [5, 0, 8, 4, 2, 1, 7, 3, 6]
    end = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    start_time = time.time()
    path = a_star_search(start, end)
    end_time = time.time()

    for m in path:
        print(m)
        print()

    print('Steps to goal: {0}'.format(len(path) - 1))
    print("Execution Time= ", (end_time - start_time) * 1000, "ms")

if __name__ == "__main__":
    main()
