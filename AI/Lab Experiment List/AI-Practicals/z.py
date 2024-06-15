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

    def generate_all_successors(self, w, checked):
        child_list = []
        for r in range(1, 9):
            result = self.apply_rule(r, w)
            if result is not None and (result.x, result.y) not in checked:
                checked.add((result.x, result.y))
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

    def execution(self):
        checked = set()
        space = 0
        queue = deque([self.initial_state])
        while queue:
            current_state = queue.popleft()
            space += 1
            if (current_state.x == self.w.target.x or self.w.target.x < 0) and (
                    current_state.y == self.w.target.y or self.w.target.y < 0):
                print("Total Nodes Explored:", space + len(queue))
                return current_state
            else:
                queue.extend(current_state.generate_all_successors(self.w, checked))
        print("Total Nodes Explored:", space + len(queue))
        return None


def display(node):
    path = []
    while node:
        path.append([node.x, node.y])
        node = node.parent
    path.reverse()
    print("Your path is:", "->".join(["[{}, {}]".format(coord[0], coord[1]) for coord in path]))


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
    start_time = time.time()
    bfs = BFSSearch(initial, w)
    obj = bfs.execution()
    end_time = time.time()
    print("Time taken with BFS:", (end_time - start_time) * 1000, "milliseconds")
    if obj is not None:
        display(obj)
    else:
        print("No solution possible.")


get_user_input()
