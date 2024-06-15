import time
from collections import deque

class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    def apply_rule(self, rule_no, w):
        if rule_no == 1:
            return Node(w.jug1_capacity, self.y, self)
        elif rule_no == 2:
            return Node(self.x, w.jug2_capacity, self)
        elif rule_no == 3:
            return Node(0, self.y, self)
        elif rule_no == 4:
            return Node(self.x, 0, self)
        elif rule_no == 5:
            diff = min(self.x + self.y, w.jug1_capacity) - self.x
            return Node(self.x + diff, self.y - diff, self)
        elif rule_no == 6:
            diff = min(self.x + self.y, w.jug2_capacity) - self.y
            return Node(self.x - diff, self.y + diff, self)
        elif rule_no == 7:
            return Node(self.x + self.y, 0, self)
        elif rule_no == 8:
            return Node(0, self.x + self.y, self)
        else:
            return None

    def generate_all_successors(self, w, visited):
        child_list = []
        for r in range(1, 9):
            result = self.apply_rule(r, w)
            if result is not None and (result.x, result.y) not in visited:
                visited.add((result.x, result.y))
                child_list.append(result)
        return child_list


class WaterJug:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target


class BFSSearch:
    def __init__(self, initial_state, w):
        self.initial_state = initial_state
        self.w = w

    def execute(self):
        visited = set()
        queue = deque([self.initial_state])
        visited.add((self.initial_state.x, self.initial_state.y))  # Add initial state to visited
        start_time = time.time()
        while queue:
            current_state = queue.popleft()
            if (current_state.x == self.w.target.x or self.w.target.x < 0) and (
                    current_state.y == self.w.target.y or self.w.target.y < 0):
                end_time = time.time()
                return current_state, len(visited), end_time - start_time
            else:
                successors = current_state.generate_all_successors(self.w, visited)
                queue.extend(successors)
                # Update visited set
                for succ in successors:
                    visited.add((succ.x, succ.y))
        return None, len(visited), 0


def display(node):
    path = []
    while node:
        path.append([node.x, node.y])
        node = node.parent
    path.reverse()
    print("Your path is:", "->".join(["[{}, {}]".format(coord[0], coord[1]) for coord in path]))


def test(initial_state, w):
    print("Starting manual execution...")
    current_state = initial_state
    visited = set()
    while True:
        print(f"Current State: ( {current_state.x} , {current_state.y} )")
        user_input = input("Enter 'Q' to quit or Rule No. to apply: ").strip().upper()
        if user_input == 'Q':
            break
        elif user_input == '':
            print("Error: Please enter a valid rule number (1-8) or 'Q' to quit.")
            continue
        elif not user_input.isdigit() or int(user_input) not in range(1, 9):
            print("Error: Please enter a valid rule number (1-8) or 'Q' to quit.")
            continue
        rule_no = int(user_input)
        obj = current_state.apply_rule(rule_no, w)
        if obj:
            current_state = obj
            visited.add((current_state.x, current_state.y))
            if (current_state.x == w.target.x or w.target.x < 0) and (
                    current_state.y == w.target.y or w.target.y < 0):
                print("Goal state reached!")
                print(f"Final State: ( {current_state.x} , {current_state.y} )")
                break
        else:
            print("Rule can't apply")
    return len(visited)


def get_user_input():
    jug1_capacity = int(input("Enter the capacity of jug1: "))
    jug2_capacity = int(input("Enter the capacity of jug2: "))
    target_x = int(input("Enter the target amount of water in Jug 1. If none, enter -1: "))
    target_y = int(input("Enter the target amount of water in Jug 2. If none, enter -1: "))
    if jug1_capacity < 1 or jug2_capacity < 1:
        print("Capacity can't be less than 1")
        return
    elif jug1_capacity < target_x or jug2_capacity < target_y:
        print('Your target is more than your jug capacity')
        return

    w = WaterJug(jug1_capacity, jug2_capacity, Node(target_x, target_y, None))
    initial = Node(0, 0, None)

    while True:
        manual_input = input("Do you want to perform manual execution? (y/n): ").strip().lower()
        if manual_input == 'y':
            start_time = time.time()
            visited_nodes = test(initial, w)
            end_time = time.time()
            print("Time taken for manual execution:", (end_time - start_time) * 1000, "milliseconds")
            print("No. of Visited Nodes:", visited_nodes)
            break
        elif manual_input == 'n':
            bfs = BFSSearch(initial, w)
            obj, visited_nodes, execution_time = bfs.execute()
            if obj is not None:
                print("Time taken with BFS:", execution_time * 1000, "milliseconds")
                display(obj)
                print("No. of Visited Nodes during BFS:", visited_nodes)
            else:
                print("No solution possible.")
            break
        else:
            print("Invalid input! Please enter 'y' for manual execution or 'n' for automatic execution.")


get_user_input()
