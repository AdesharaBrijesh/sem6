import time

class Node:
    def __init__(self, x, y, parent):
        self.x = x  # Water in jug1
        self.y = y  # Water in jug2
        self.parent = parent  # Parent node

class BFSAlgo:
    def __init__(self, jug1_capacity, jug2_capacity, goal):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.goal = goal

    def get_path(self, node):
        path = []
        while node:
            path.append((node.x, node.y))
            node = node.parent
        return path[::-1]

    def is_valid(self, x, y):
        return 0 <= x <= self.jug1_capacity and 0 <= y <= self.jug2_capacity

    def explore_neighbors(self, node, visited, queue):
        x, y = node.x, node.y

        # All possible operations: Fill jug1, fill jug2, empty jug1, empty jug2, pour jug1 to jug2, pour jug2 to jug1
        operations = [(self.jug1_capacity, y), (x, self.jug2_capacity), (0, y), (x, 0),
                      (min(x + y, self.jug1_capacity), max(0, x + y - self.jug1_capacity)),
                      (max(0, x + y - self.jug2_capacity), min(x + y, self.jug2_capacity))]

        for operation in operations:
            new_x, new_y = operation
            if (new_x, new_y) not in visited and self.is_valid(new_x, new_y):
                new_node = Node(new_x, new_y, node)
                queue.append(new_node)
                visited.add((new_x, new_y))

    def bfs(self):
        start_time = time.time()

        # Initialize the queue with initial state
        initial_node = Node(0, 0, None)
        queue = [initial_node]
        visited = {(0, 0)}

        while queue:
            node = queue.pop(0)

            if node.x == self.goal or node.y == self.goal or node.x + node.y == self.goal:
                path = self.get_path(node)
                execution_time = time.time() - start_time
                return path, execution_time, len(visited)

            self.explore_neighbors(node, visited, queue)

        # If no solution found
        return None, None, None

class WaterJug:
    def __init__(self):
        self.jug1_capacity = int(input("Enter the capacity of jug1: "))
        self.jug2_capacity = int(input("Enter the capacity of jug2: "))
        self.goal = int(input("Enter the goal amount of water: "))

    def solve(self):
        bfs = BFSAlgo(self.jug1_capacity, self.jug2_capacity, self.goal)
        path, execution_time, num_explored_nodes = bfs.bfs()

        if path:
            print("Steps to reach the goal:")
            for step in path:
                print(step)
            print("Execution Time:", execution_time*1000 , "ms")
            print("Number of Explored Nodes:", num_explored_nodes)
        else:
            print("No solution found.")

if __name__ == "__main__":
    water_jug = WaterJug()
    water_jug.solve()

