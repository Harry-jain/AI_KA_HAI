import copy

# Define goal state
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_position = goal_state.index(tile)
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_position, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

# Get possible neighbors by moving the empty space
def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(new_state)
    return neighbors

# Simple Hill Climbing Algorithm
def simple_hill_climbing(start_state):
    current_state = start_state
    while True:
        current_distance = manhattan_distance(current_state)
        neighbors = get_neighbors(current_state)
        next_state = None

        # Find a neighbor with a better (lower) heuristic value
        for neighbor in neighbors:
            if manhattan_distance(neighbor) < current_distance:
                next_state = neighbor
                break

        if next_state is None:  # No improvement found
            return current_state

        current_state = next_state

# Example usage
start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
solution = simple_hill_climbing(start_state)
print("Solution State:")
for i in range(0, 9, 3):
    print(solution[i:i+3])
