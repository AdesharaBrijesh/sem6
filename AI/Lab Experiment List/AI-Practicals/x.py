import time

class Node:
    def __init__(self, data):
        self.x = 0
        self.y = 0
        self.parent = data

    def operation(self, cnode, rule):
        x = cnode.x
        y = cnode.y

        if rule == 1:
            if x < max_jug1:
                x = max_jug1
            else:
                return None
        elif rule == 2:
            if y < max_jug2:
                y = max_jug2
            else:
                return None
        elif rule == 3:
            if x > 0:
                x = 0
            else:
                return None
        elif rule == 4:
            if y > 0:
                y = 0
            else:
                return None
        elif rule == 5:
            if x + y >= max_jug1:
                y = y - (max_jug1 - x)
                x = max_jug1
            else:
                return None
        elif rule == 6:
            if x + y >= max_jug2:
                x = x - (max_jug2 - y)
                y = max_jug2
            else:
                return None
        elif rule == 7:
            if x + y < max_jug1:
                x = x + y
                y = 0
            else:
                return None
        elif rule == 8:
            if x + y < max_jug2:
                y = x + y
                x = 0
            else:
                return None

        if x == cnode.x and y == cnode.y:
            return None

        next_node = Node(cnode)
        next_node.x = x
        next_node.y = y
        next_node.parent = cnode
        return next_node

class SearchBFS:
    def __init__(self, initial_node, goal_node):
        self.queue = []
        self.queue.append(initial_node)
        self.goal_node = goal_node

    def pop_node(self):
        return self.queue.pop(0)

    def search(self):
        while len(self.queue) != 0:
            c_node = self.pop_node()

            if c_node.x == self.goal_node.x and c_node.y == self.goal_node.y:
                return c_node
            successors = self.generate_all_successors(c_node)
            self.queue.extend(successors)
        return None

    def generate_all_successors(self, c_node):
        successors = []
        for rule in range(1, 9):
            next_node = c_node.operation(c_node, rule)
            if next_node is not None:
                successors.append(next_node)
        return successors

    def print_path(self, c_node):
        temp = c_node
        path = []
        while temp is not None:
            path.append(temp)
            temp = temp.parent

        path.reverse()
        for node in path:
            print("(", node.x, ",", node.y, ")")
        print("Path cost:", len(path))

max_jug1 = int(input("Enter the maximum capacity of Jug 1: "))
max_jug2 = int(input("Enter the maximum capacity of Jug 2: "))
initial_node = Node(None)
initial_node.x = 0
initial_node.y = 0
initial_node.parent = None
goal_node = Node(None)
goal_node.x = int(input("Enter the desired amount of water in Jug 1: "))
goal_node.y = 0
goal_node.parent = None

print("\nBFS algorithm is running...")
start_time = time.time()
solution = SearchBFS(initial_node, goal_node)
solution_node = solution.search()
end_time = time.time()

if solution_node is not None:
    print("Solution found:")
    solution.print_path(solution_node)
else:
    print("No solution found")

execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
print("Executed in time:", execution_time, "ms")
