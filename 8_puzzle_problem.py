import copy
from heapq import heappush, heappop

# Directions
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]
directions = ["Down", "Left", "Up", "Right"]

# PriorityQueue for A* algorithm
class PriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self, item):
        heappush(self.heap, item)
    def pop(self):
        return heappop(self.heap)
    def empty(self):
        return len(self.heap) == 0

# Node representing each state of the puzzle
class Node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level, move_direction):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level
        self.move_direction = move_direction
    def __lt__(self, other):
        return self.cost < other.cost

# Heuristic function to calculate misplaced tiles
def calculateCost(mat, final) -> int:
    return sum(1 for i in range(len(mat)) for j in range(len(mat)) if mat[i][j] and mat[i][j] != final[i][j])

# Create a new node by moving the empty tile
def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final, move_direction) -> Node:
    new_mat = copy.deepcopy(mat)
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    cost = calculateCost(new_mat, final)
    return Node(parent, new_mat, new_empty_tile_pos, cost, level, move_direction)

# Print matrix
def printMatrix(mat):
    for row in mat:
        print(' '.join(map(str, row)))
    print()

# Check if position is valid
def isSafe(x, y, n):
    return 0 <= x < n and 0 <= y < n

# Print the solution path
def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    if root.move_direction:
        print(f"Move: {root.move_direction}")
    printMatrix(root.mat)

# A* algorithm to solve the puzzle
def solve(initial, empty_tile_pos, final):
    n = len(initial)
    pq = PriorityQueue()
    root = Node(None, initial, empty_tile_pos, calculateCost(initial, final), 0, None)
    pq.push(root)

    while not pq.empty():
        minimum = pq.pop()
        if minimum.cost == 0:
            printPath(minimum)
            return

        for i in range(4):
            new_tile_pos = [minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i]]
            if isSafe(new_tile_pos[0], new_tile_pos[1], n):
                move_direction = directions[i]
                child = newNode(minimum.mat, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1, minimum, final, move_direction)
                pq.push(child)

if __name__ == "__main__":
    n = int(input("Enter the size of the matrix (e.g., 3 for 3x3): "))
    print("Enter the initial matrix:")
    initial = [list(map(int, input().split())) for _ in range(n)]
    print("Enter the final matrix:")
    final = [list(map(int, input().split())) for _ in range(n)]

    empty_tile_pos = next((i, j) for i in range(n) for j in range(n) if initial[i][j] == 0)
    solve(initial, empty_tile_pos, final)
